from email import message
from django.shortcuts import render,redirect

from App.models import EmployeeTable
from App.forms import EmployeeForm
from App.forms import ContactForm

from App.forms import RegisterForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def register_view(request):

    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

    
    
        if User.objects.filter(username=name):
            messages.warning(request, "Username already exist! Please try some other username.")
            return redirect('Register')
        
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email Already Registered!!")
            return redirect('Register')
        
        if len(name)>20:
            messages.warning(request, "Username must be under 20 charcters!!")
            return redirect('Home')
        
        if password1 != password2:
            messages.warning(request, "Passwords didn't matched!!")
            return redirect('Register')
        
        if not name.isalnum():
            messages.warning(request, "Username must be Alpha-Numeric!!")
            return redirect('Register')
        if len(password1)<8:
            messages.warning(request, "Password must contain at least 8 character !!")
            return redirect('Register')
        user = User.objects.create_user(username=name,email=email,password=password1)
        user.save()
        messages.success(request,'Your Account has been Registered Successfully!!!.....')
        return redirect('Login')
    else:
        form=RegisterForm
        return render(request,'register.html',{'form':form})



def login_view(request):

    if request.user.is_authenticated:
        messages.info(request,'You are Logged in Successfully!!!...')
        return redirect('Home')
    
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,' Login Successfully!!!...')
            return redirect('Home')

        else:
            messages.warning(request,'Could not authenticate, Check Credential')
    return render(request,'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request,'Logout  Successfully!!!...')
    return redirect('Login')

@login_required
def home(request):
    
    return render(request,'home.html')

@login_required
def insert(request):
    if request.method =='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(request,'Employee Details Inserted Successfully!!!...')
                return redirect('Insert')
            except:
                messages.warning(request,'Something Went Wrong!!!...')
                return redirect('Insert')
    else:
        form = EmployeeForm
        return render(request,'insert.html',{'form':form})

@login_required
def details(request):

    data= EmployeeTable.objects.all()
    return render(request,'details.html',{'data':data})

def update(request):
    data= EmployeeTable.objects.all()
    return render(request,'update.html',{'data':data})


@login_required
def update2(request,id):
    data = EmployeeTable.objects.get(id=id)

    if request.method == 'POST':
        name     = request.POST['name']
        age      = request.POST['age']
        salary   = request.POST['salary']
        position = request.POST['position']
        contact  = request.POST['contact']
        address  = request.POST['address']

        data.Empname=name
        data.Age=age
        data.Salary=salary
        data.Position=position
        data.Contact=contact
        data.Address=address
        data.save()
        messages.success(request,'Updated Details Successfullly!!!...')
        return redirect('Update')
        
    return render(request,'update2.html',{'data':data})

@login_required
def delete(request):
    data= EmployeeTable.objects.all()
    return render(request,'delete.html',{'data':data})


@login_required
def delete2(request,id):
    data = EmployeeTable.objects.get(id=id)
    data.delete()
    messages.success(request,'Deleted Details Successfully!!!...')
    return redirect('Delete')

@login_required
def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(request,'Message Sent Successfully!!!...')
                return redirect('Contact')
            except:
                messages.warning(request,'Something Went Wrong!!!...')
                return redirect('Contact')
    else:
        form = ContactForm
        return render(request,'contact.html',{'form':form})

@login_required
def about(request):
    return render(request,'about.html')
