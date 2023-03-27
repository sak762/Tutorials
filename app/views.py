from django.shortcuts import render,redirect
from django.contrib import messages
from app.auth import authentication, input_verification
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from app.models import Crop_Details
import numpy as np
import pickle
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, "index.html", {'navbar' : 'home'})

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        # print(first_name, contact_no, ussername)
        verify = authentication(first_name, last_name, password, password1)
        if verify == "success":
            user = User.objects.create_user(username, password, password1)          #create_user
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, "Your Account has been Created.")
            return redirect("/")
            
        else:
            messages.error(request, verify)
            return redirect("register")
            # return HttpResponse("This is Home page")
    return render(request, "register.html", {'navbar' : 'register'})

def log_in(request):
    if request.method == "POST":
        # return HttpResponse("This is Home page")  
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Log In Successful...!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid User...!")
            return redirect("log_in")
    return render(request, "log_in.html", {'navbar' : 'log_in'})

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def log_out(request):
    logout(request)
    messages.success(request, "Log out Successfuly...!")
    return redirect("/")

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def dashboard(request):
    context = {
        'first_name': request.user.first_name, 
        'last_name': request.user.last_name, 
    }
    
    return render(request, "dashboard.html", context)


@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def crop_report(request):
    crop_data = Crop_Details.objects.last()
    context = {
        'first_name': request.user.first_name, 
        'last_name': request.user.last_name, 
        'crop_data' : crop_data
    }
    
    return render(request, "crop_report.html", context)

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def report(request):
    crop_data = Crop_Details.objects.last()
    context = { 
        'crop_data' : crop_data
    }
    return render(request, "report.html", context)