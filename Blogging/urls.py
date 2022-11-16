from django.urls import path
from . import views

urlpatterns=[
    path('/home',views.Home,name='home'),
    path('/signup',views.User_SignUp,name='signup'),
    path('/login',views.User_Login,name='login'),
    path('/logout',views.User_Logout,name='logout'),
    path('/contact',views.Contact,name='contact'),
    path('/thanks',views.Thanks,name='thanks'),
    path('/add',views.add_Blogs.as_view(),name='add'),
    path('/update/<int:id>/',views.update_Blogs.as_view(),name='update'),
    path('/delete/<int:id>/',views.delete_Blogs.as_view(),name='delete'),
    path('/about',views.About,name='about'),
    path('/pro',views.User_Profile,name='pro'),
    #Cookies PAth
    path('/set',views.set_Blog_cookies,name='set'),
    path('/get',views.get_Blog_cookies,name='get'),
    path('/del',views.del_Blog_cookies,name='del'),
    path('/session',views.set_Blog_session,name='session'),
    path('/get_session',views.get_Blog_session,name='get_session'),
    path('/del_session', views.del_Blog_session, name='del_session'),
    path('/excep',views.excep,name='ex'),
    path('/user',views.user,name='user'),


    #CBV
    path('/add',views.add_Blogs.as_view(),name='add'),
    path('/update/<int:id>/',views.update_Blogs.as_view(),name='update'),
    path('/delete/<int:id>/',views.delete_Blogs.as_view(),name='delete'),

]