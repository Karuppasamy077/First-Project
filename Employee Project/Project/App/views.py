from email import message
from django.shortcuts import render,redirect
from App.models import EmployeeTable
from App.forms import EmployeeForm
from django.contrib import messages
from App.forms import ContactForm

# Create your views here.

def home(request):
    
    return render(request,'home.html')

def details(request):

    data= EmployeeTable.objects.all()
    return render(request,'details.html',{'data':data})

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
      
def update(request):
    data= EmployeeTable.objects.all()
    return render(request,'update.html',{'data':data})



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

def delete(request):
    data= EmployeeTable.objects.all()
    return render(request,'delete.html',{'data':data})


def delete2(request,id):
    data = EmployeeTable.objects.get(id=id)
    data.delete()
    messages.success(request,'Deleted Details Successfully!!!...')
    return redirect('Delete')

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

def about(request):
    return render(request,'about.html')
