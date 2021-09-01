from django.shortcuts import render, redirect
# # from django.http import HttpResponse
from datetime import datetime
from app1.models import Contact
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')


def home(request):
    return redirect('/')

def about_us(request):
    return render(request,'about_us.html')

def books(request):
    if request.user.is_anonymous:
        messages.warning(request, 'You must login first to read books !')
        return redirect('/')
    return render(request,'books.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        queries = request.POST.get('queries')
        tell_us = request.POST.get('tell_us')
        contact = Contact(name=name, email=email, queries=queries,
        tell_us=tell_us, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent !')
    return render(request,'contact.html')

def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,
        email=email,password=password)
        user.save()
        messages.success(request, 'Congratulations ! Profile created. Now you can login here.')
        return redirect('/')
    else:
        return redirect('/')

def SignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Congratulations ! You are logged In.')
            return redirect('/')
        else:
            messages.warning(request, 'You must have entered wrong username or password !')
            return redirect('/')

    else:
        return redirect('/')

def LogOut(request):
    auth.logout(request)
    messages.success(request, 'Congratulations ! You logged out successfully.')
    return redirect('/')
