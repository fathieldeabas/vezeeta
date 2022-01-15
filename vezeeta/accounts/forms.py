from cProfile import label
from dataclasses import fields
import email
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class Login_Form(forms.ModelForm):
    username= forms.CharField(label='الاسم')
    password= forms.CharField(label='كلمه السر',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password')

class UserCreationForms(UserCreationForm):
    username= forms.CharField(label='الاسم')
    first_name= forms.CharField(label=' الاسم الاول')
    last_name= forms.CharField(label=' الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')
    password1= forms.CharField(label='كلمه السر',widget=forms.PasswordInput())
    password2= forms.CharField(label='تاكيد كلمه السر ',widget=forms.PasswordInput())

    class Meta:
        model= User
        fields=('username','first_name','last_name','email','password1','password2')

class Update_Profile( forms.ModelForm):
    first_name= forms.CharField(label=' الاسم الاول')
    last_name= forms.CharField(label=' الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')

    class Meta:
        model=User
        fields=('first_name','last_name','email')

class Update_Profile2(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields=('name','subtitle',
        'address','address_details' ,
        'number_phone',
        'working_hours',
        'waiting_time',
        'doctor',
        'specialist_doctor'
        ,'who_i',
        'price','image'
        ,'facebook','twitter','google')