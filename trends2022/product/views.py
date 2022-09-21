from socket import MsgFlag
from unicodedata import name
from django.shortcuts import render,redirect

from .models import accesories,comment_box


def about(request):
    id=request.GET['id']
    pro=accesories.objects.get(id=id)
    return render(request,"about.html",{'key1':pro})

def comment(request):
    name=request.POST['user']
    id=request.POST['pro']
    message=request.POST['msg']
    cmt=comment_box.objects.create(name=name,msg=message,fkey_id=id)
    cmt.save();
    return redirect("/")