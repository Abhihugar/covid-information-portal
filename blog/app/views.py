from django.shortcuts import render,redirect
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
# import matplotlib.pyplot as plt

import pandas as pd
import time
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,permission_required
from.models import Contact_us
# Create your views here.
def base(request):
    return render(request,'base.html')



def about(request):
    return render(request,'about.html')


# def signup(request):
#     return render(request,"signup.html")


def login(request):
    return render(request,"login.html")


def contact(request):
    return render(request,'contact.html')

def helpline(request):
    return render(request,'helpline.html')

def vaccine(request):
    return render(request,'vaccine.html')

def covid(request):
    # if not request.user.is_authenticated:
    #     messages.warning(request,"Please Login and Try Again")
    #     return redirect('/')
    return render(request,'covid.html')


def donation(request):
    return render(request,'donation.html')

def vfaq(request):
    return render(request,'vfaq.html')


def signup(request):
    return render(request,'signup.html')

def handlesignup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]

        if len(username)>10:
            messages.warning(request,"username should be less than 10 characters")
            return redirect("/")
        if not username.isalnum():
            messages.warning(request,"username should contain only numbers and letters")

        if(pass1!=pass2):
            messages.warning(request,"password is Incorrect")
            return redirect("login.html")
        try:
            if User.objects.get(username=username):
                messages.warning(request,"username is already taken")
                return redirect("/")
        except Exception as identifier:
            pass


        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"signup successfull please login")

        return redirect("login.html")
    return render(request,"signup.html")


    
def handlelogin(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["pass1"]
        user=authenticate(email=email,pass1=password)
        if user is not None:
            login(request,user)
            messages.info(request,"<h2>login successfull</h2>")
            return redirect("/")
        else:
            messages.error(request,"invalid credentials")
            return redirect("/")

    return render(request,"base.html")

def handlelogout(request):
    logout(request)
    return render(request,"base.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")

        data=Contact_us(name=name,email=email,desc=desc)
        data.save()
        messages.success(request, 'message sent successfully')
        return redirect("/")
    return render(request,"contact.html")


def Blog(request):
    blog=Blog.objects.all()
    context={
        "blogn":blog
    }

    return render(request,"covid.html",context)