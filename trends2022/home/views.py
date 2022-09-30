import email
from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from product.models import accesories

a="php"
m="testing"

def index(request):
    if request.method=='POST':
        pname=request.POST['search']
        pro=accesories.objects.filter(name__istartswith=pname)
        return render(request,"index.html",{'pro':pro})
    else:
        pro=accesories.objects.all()
        if 'username' in request.COOKIES:
            ukey=request.COOKIES['username']
            return render(request,"index.html",{'pro':pro,'ukey':ukey})
        else:
            return render(request,"index.html",{'pro':pro})
        

def samp(request):
    return render(request,"test.html",{'l':a,'j':m})


def login1(request):
    if request.method=='POST':
        name=request.POST['uname']
        password=request.POST['iname']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            response=redirect('/')
            response.set_cookie('username',name)
            return response            
        else:
            msg="Invalid username or Password"
            return render(request,"login.html",{'msg':msg})
    else:
        return render(request,"login.html")



def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']
        uchk=User.objects.filter(username=username)
        echk=User.objects.filter(email=email)
        print(uchk)
        if uchk:
            msg="Username is already taken"
            return render(request,"register.html",{'msg':msg,})
  
        elif echk:
            msg="Email is already taken"
            return render(request,"register.html",{'msg':msg,})
    
        elif password!=repassword:
            msg="Invalid password"
            return render(request,"register.html",{'msg':msg,})
        
        else:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            user.save();
            auth.login(request,user)
            return redirect('/')
    else:
        return render(request,"register.html")    

def logout(request):
    auth.logout(request)
    resp=redirect("/")
    resp.delete_cookie('username')
    return (resp)
