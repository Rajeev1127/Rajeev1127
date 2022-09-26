from socket import MsgFlag
from unicodedata import name
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from .models import accesories,comment_box


def about(request):
    if request.method=='POST':
        pro_name=request.POST['search']
        pro=accesories.objects.get(name=pro_name)
    else:
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


def search(request):
    if "term" in request.GET:
        name=request.GET['term']

        product=accesories.objects.filter(name__istartswith=name)
    
        l=[]
        for i in product:
            l.append(i.name)

        return JsonResponse(l,safe=False)
    return render(request,"test.html")