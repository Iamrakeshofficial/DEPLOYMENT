from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.template.response import TemplateResponse
from .forms import SignUpForm,ContactForm,BlogForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Blogger,Blog
from django.contrib.auth.models import User,Group
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.core.cache import cache
from django.core.mail import send_mail

from django.views.generic.base import TemplateView,RedirectView
from django.views import View


# Create your views here.

def Home(request):
    blogs=Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def About(request):
    return render(request,'about.html')

def User_SignUp(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            Email=fm.cleaned_data['email']
            messages.success(request,'Successfully Registered')
            send_mail(' Registration Successfull', 'Signup and Registration Was Successfull Congratulations Now You can read and Write Blogs On My Website.',
                      'iamrakeshofficial143@gmail.com', [str(Email)], fail_silently=False)
            print("Form is Validated...")
            print("Email sent was SuccessFull...")
            user = fm.save()
            group = Group.objects.get(name='OJAS_BLOG')
            user.groups.add(group)
            return HttpResponseRedirect('/')
    else:
        fm=SignUpForm()
    return render(request,'signup.html',{"form":fm})


def User_Login(request):
    print(request.user)
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                un=fm.cleaned_data['username']
                up=fm.cleaned_data['password']
                user=authenticate(username=un,password=up)

                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')

                    return HttpResponseRedirect('/home/pro')

        else:
            fm=AuthenticationForm()
        return render(request,'login.html',{"form":fm})
    else:
        return HttpResponseRedirect('/home/home')



def User_Logout(request):
  logout(request)
  messages.success(request,"Successfully Logout")
  return HttpResponseRedirect('/home/login')



def Contact(request):
    if request.method=='POST':
        fm=ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            print("Form is Validated")
            return HttpResponseRedirect('/home/thanks')

    else:
        fm=ContactForm()
    return render(request,'contact.html',{"form":fm})

def Thanks(request):
    return render(request,'thanks.html')

# def add_Blogs(request):
#     if request.method == 'POST':
#         fm=BlogForm(request.POST)
#         if fm.is_valid():
#             print('Form is Validated')
#             ti=fm.cleaned_data['title']
#             des=fm.cleaned_data['description']


#             ob=Blog(title=ti,description=des)
#             ob.save()
#             fm=BlogForm()

#             ob1=Blog.objects.all()
#             return HttpResponseRedirect('/home/home',{"form":fm,"ob1":ob1})
#     else:
#         fm=BlogForm()
#     ob1 = Blog.objects.all()


#     return render(request,'add_blog.html',{"form":fm,"ob1":ob1})


#CLASS BASED VIEWS

class add_Blogs(TemplateView):
    template_name='add_blog.html'

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        fm=BlogForm()
        ob1=Blog.objects.all()
        context={"form":fm,"ob1":ob1}
        return context

    def post(self,request):
        fm=BlogForm(request.POST)
        if fm.is_valid():
            print('Form is Validated')
            ti=fm.cleaned_data['title']
            des=fm.cleaned_data['description']


            ob=Blog(title=ti,description=des)
            ob.save()
            ob1=Blog.objects.all()
            return HttpResponseRedirect('/home/home',{"form":fm,"ob1":ob1})

# def update_Blogs(request,id):
#     if request.method=='POST':
#         ab=Blog.objects.get(pk=id)
#         fm=BlogForm(request.POST,instance=ab)

#         if fm.is_valid():
#             fm.save()
#         return HttpResponseRedirect('/home/add')

#     else:
#         ab=Blog.objects.get(pk=id)
#         fm=BlogForm(instance=ab)
#     return render(request,'update_blog.html',{"form":fm})


#CLASS BASED VIEWS

class update_Blogs(View):
    def get(self,request,id):
        ab=Blog.objects.get(pk=id)
        fm=BlogForm(instance=ab)
        return render(request,'update_blog.html',{"form":fm})

    def post(self,request,id):
        ab=Blog.objects.get(pk=id)
        fm=BlogForm(request.POST,instance=ab)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/home/add')




# def delete_Blogs(request,id):
#     if request.method=='POST':
#         ab=Blog.objects.get(pk=id)
#         ab.delete()

#     return HttpResponseRedirect('/home/add')



#CLASS BASED VIEWS

class delete_Blogs(RedirectView):
    url='/home/add'

    def get_redirect_url(self, *args ,**kwargs):
       ab=kwargs['id']
       Blog.objects.get(pk=ab).delete()

       return super().get_redirect_url(*args, **kwargs)



def User_Profile(request):
    if request.user.is_authenticated:
        blogs=Blog.objects.all()
        user = request.user
        full_name = user.get_full_name()
        group=Group.objects.all()
        ip = request.session.get('ip')
        ct =cache.get('count', version=user.pk)
        return render(request,'profile.html',{'name':request.user,'blogs':blogs, 'full_name':full_name, 'group':group,'ip':ip,'ct':ct})
    else:
        return HttpResponseRedirect('/home/log')


#COOKIES AND SESSIONS
def set_Blog_cookies(request):
    response=render(request,'blog_cookie.html')
    # response.set_cookie('name','Rakesh Kumar',max_age=50)
    # signed_cookie
    response.set_signed_cookie('name','Akash',salt='Love',expires=datetime.utcnow()+timedelta(days=2))
    return response

def get_Blog_cookies(request):
    # name=request.COOKIES['name']
    # name=request.COOKIES.get('name')
    # name=request.COOKIES.get('name',"Laxmi")
    name=request.get_signed_cookie('name',default='Harish',salt='Hello')

    return render(request,'get_blog_cookie.html',{'name':name})

def del_Blog_cookies(request):
    response= render(request,'del_Blog_cookies.html')
    response.delete_cookie('name')
    return response

# SESSION

def set_Blog_session(request):
    request.session['name']='Rakesh'
    # request.session['mname']='Kumar'
    # request.session.set_expiry(10)
    request.session.set_test_cookie()
    return render(request,'set_session.html')

def get_Blog_session(request):
    # name=request.session['name']
    name=request.session.get('name')
    # mname=request.session.get('mname')
    # keys=request.session.keys()
    # items=request.session.items()
    # age=request.session.setdefault('age','23')
    #
    # return render(request,'get_session.html',{'name':name,'mname':mname,'keys':keys,'items':items,'age':age})


    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_age())
    # print(request.session.get_expiry_date())
    # print(request.session.get_expire_at_browser_close())

    print(request.session.test_cookie_worked())
    return render(request, 'get_session.html', {'name': name})

def del_Blog_session(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    # request.session.clear_expired()

    request.session.clear_expired()


    return render(request,'del_session.html')

def excep(request):
    print("I am Excp View")

    print(10/0)
    return HttpResponse("This is Excp Page")

def user(request):
    print("I am User Info View")
    context = {'name':'Rakesh'}
    return TemplateResponse(request, 'user.html', context)


