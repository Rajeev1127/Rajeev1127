from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name="Homepage"),
    path('samp/',views.samp, name="Testpage"),
    path('login1/',views.login1, name="login"),
    path('register/',views.register, name="register"),
    path('logout/',views.logout, name="Logout")
        ]