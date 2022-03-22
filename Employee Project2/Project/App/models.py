from email.message import Message
from django.db import models

# Create your models here.

class EmployeeTable(models.Model):
    Empname = models.CharField(max_length=20)
    Age = models.IntegerField()
    Salary = models.IntegerField()
    Position = models.CharField(max_length=20)
    Contact = models.IntegerField()
    Address = models.CharField(max_length=30)


class Contactus(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    MobileNumber = models.IntegerField()
    Message = models.TextField(max_length=100)
    Timenow = models.DateTimeField(auto_now=True,blank=True)


     