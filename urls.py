from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Home', views.home, name='home'),
    path('AboutUs', views.about_us, name='about_us'),
    path('Books', views.books, name='books'),
    path('ContactUs', views.contact_us, name='contact_us'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('SignIn', views.SignIn, name='SignIn'),
    path('LogOut', views.LogOut, name='LogOut'),



]
