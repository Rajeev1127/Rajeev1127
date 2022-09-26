from django.urls import path
from . import views 

urlpatterns = [
    path('',views.about, name="about"),
    path('cmt/',views.comment, name="comment"),
    path('srh/',views.search, name="find"),
              ]