from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name="Homepage"),
    path('samp/',views.samp, name="Testpage"),
    path('login1/',views.login1, name="Loginpage"),
    path('register/',views.register, name="Registerpage"),
    path('login1/logincheck/',views.logincheck, name="Logincheck"),
    path('register/registercheck/',views.registercheck, name="Registercheck"),
    ]