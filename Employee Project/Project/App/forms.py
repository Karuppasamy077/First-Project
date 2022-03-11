from logging import PlaceHolder
from django import forms
from App.models import EmployeeTable,Contactus

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeTable
        fields ='__all__'



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields ='__all__'