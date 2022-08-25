import email
from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

a="php"
m="testing"

def index(request):
    return render(request,"index.html")


def samp(request):
    return render(request,"test.html",{'l':a,'j':m})


def login1(request):
    return render(request,"login.html")


def register(request):
    return render(request,"register.html")
    


def logincheck(request):
    name=request.GET['uname']
    password=request.GET['iname']
    user=auth.authenticate(username=name,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        return redirect('/login1')

def registercheck(request):
    username=request.GET['username']
    firstname=request.GET['firstname']
    lastname=request.GET['lastname']
    email=request.GET['email']
    password=request.GET['password']
    repassword=request.GET['repassword']
    uchk=User.objects.filter(username=username)
    echk=User.objects.filter(email=email)
    print(uchk)
    if uchk:
        msg="Username is already taken"
        return render(request,"test.html",{'key1':msg,})
  
    elif echk:
        msg="Email is already taken"
        return render(request,"test.html",{'key1':msg,})
  
    elif password!=repassword:
        msg="Invalid password"
        return render(request,"test.html",{'key1':msg,})
    
    else:
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save();
        return redirect('/')
  
    
    