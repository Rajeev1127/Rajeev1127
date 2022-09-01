from distutils.command.install_egg_info import to_filename
from distutils.command.upload import upload
from pickle import TRUE
from django.db import models

class accesories(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pic")
    price=models.IntegerField()
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)