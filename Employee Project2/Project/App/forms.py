from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from App.models import EmployeeTable,Contactus


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeTable
        fields ='__all__'



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields ='__all__'