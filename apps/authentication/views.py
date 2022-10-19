# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
import os
from .models import CustomUser


def login_view(request):
    form = LoginForm(request.POST or None)
    letter = ('t', 's', 'o', 'h')
    users = CustomUser.objects.all()
    
    if request.method == "POST":
        if request.POST.get("login"):
            user_name = request.POST.get("username")
            current_user = os.getlogin()
            valid = CustomUser.objects.filter(name=user_name).exists() and CustomUser.active
            print(valid)

            if valid:
                return render(request, "home/main.html", {})

            return redirect("/register")


    else:
        return render(request, "accounts/login.html", {"form":form})




def register_user(request):
    active = CustomUser.objects.filter(active=True)
    #print(active.all)
    msg = None
    form = SignUpForm(request.POST)
    letter = ('t', 's', 'o', 'h')
    username = request.POST.get("username")
    if request.method == "POST":
        if len(username) == 8 and username.startswith(letter):
            if CustomUser.objects.filter(name=username).exists():
                msg = " The user already exists"
            else:
                user = CustomUser(name=username)
                user.save()
                return redirect("/user_list")

        else:
            msg = "In valid user"

    return render(request, "accounts/register.html", {"form":form, "msg": msg})

