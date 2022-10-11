from socket import MsgFlag
from unicodedata import name
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from .models import accesories,comment_box
from django.core.cache import cache


def about(request):
    id=request.GET['id']
    if cache.get(id):
        pro=cache.get(id)
        print("DATA FROM CACHE")
    else:
        pro=accesories.objects.get(id=id)
        cache.set(id,pro)
        print("DATA FROM DATABASE")
    return render(request,"about.html",{'key1':pro})

def about2(request):
    id=request.GET['id']
    print(id)
    pro=accesories.objects.get(id=id)

    if 'recent' in request.session:
        if id in request.session['recent']:
            request.session['recent'].remove(id)        
        print(request.session['recent'])
        recent_list=accesories.objects.filter(id__in=request.session['recent'])
        print(recent_list)        
        request.session['recent'].insert(0,id)

        if len(request.session['recent'])>4:
            request.session['recent'].pop()
    else:
         request.session['recent']=[id]
         recent_list=accesories.objects.filter(id=id)
    request.session.modified=True
    return render(request,"about.html",{'key1':pro,'key2':recent_list})

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