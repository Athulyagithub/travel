from django.contrib import messages, auth
from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.shortcuts import render, redirect

from . models import Place

# Create your views here.


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")
def detail(request):
    obj=Place.objects.all()
    return render(request,'index.html',{'result':obj})
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['cpassword']
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password,last_name=lastname,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "passwords doesn't match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')















# def home(request):
#     return HttpResponse("home page")

# def contact(request):
#     return HttpResponse("this is contact page")

# def thanks(request):
#     return HttpResponse("this is thanks page")
# def home(request):
#     return render(request,'add.html')
# def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
#    sub=x-y
#    mul=x*y
#    div=x//y
#    return render(request,'about.html',{'result':res,'subtraction':sub,
#                                        'multiplication':mul,'division':div})