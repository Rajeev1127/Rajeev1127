from django.shortcuts import render

from .models import accesories


def about(request):
    id=request.GET['id']
    pro=accesories.objects.get(id=id)
    print(pro)
    return render(request,"about.html",{'key1':pro})