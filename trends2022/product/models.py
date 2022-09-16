from distutils.command.install_egg_info import to_filename
from distutils.command.upload import upload
from pickle import TRUE
from tkinter import CASCADE
from django.db import models

class accesories(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pic")
    price=models.IntegerField()
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

class comment_box(models.Model):
    fkey=models.ForeignKey(accesories,realted_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    msg=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    