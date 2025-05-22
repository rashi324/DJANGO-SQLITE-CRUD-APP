from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.forms import *

#create your views here.

def signup(request):
    if request.method=='POST':
        form=NewUserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
           
    else:
        form=NewUserForm()
    return render(request,'signup.html',{'form':form})

def loginpage(request):
    if request.method=='POST':
        usr=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(request,username=usr,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password not correct try Again')
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def addemployee(request):
    if request.method=='POST':
        form=AddEmployeeFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=AddEmployeeFrom()
    return render(request,'addemployee.html',{'form':form})

def viewemployee(request):
    employees=Employee.objects.all()
    return render(request,'viewemployee.html',{'employees':employees})

def deleteemployee(request, empid):
    data = Employee.objects.get(empid=empid)
    data.delete()
    employees = Employee.objects.all()
    return render(request, 'viewemployee.html', {'employees': employees})


def editemployee(request,empid):
    data=Employee.objects.get(empid=empid)
    return render(request,'editemployee.html',{'data':data})

def updateemployee(request,empid):
    data=Employee.objects.get(empid=empid)
    form=AddEmployeeFrom(request.POST,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        return redirect('viewemployee')
    else:
     return render(request,'editemployee.html',{'data':data})
