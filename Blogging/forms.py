from django import forms
from .models import Blogger,Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Confirm Password (again.)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={'email':'Email'}
        error_messages = {
            'username': {'required': 'Give your name'}}

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),



        }


class ContactForm(forms.ModelForm):
    class Meta:
        model=Blogger
        fields=['name','email','subject','message']
        labels = {'name': 'Enter Name', 'email': 'Enter EMail','subject':'Enter Subject'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message':forms.Textarea(attrs={'class': 'form-control'}),


                }

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','description']
        label={'title':'Title','description':'Description'}

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

            }