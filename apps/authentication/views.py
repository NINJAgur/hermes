# Create your views here.
from faulthandler import disable
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import os
from .models import CustomUser


def login_view(request):
    msg = None
    form = LoginForm(request.POST or None)
    letter = ('t', 's', 'o', 'h')
    users = CustomUser.objects.all()
    
    if request.method == "POST":
        if request.POST.get("login"):
            user_name = request.POST.get("username")
            current_user = os.getlogin()
            
            if User.objects.filter(username=user_name).exists():
                user_a = User.objects.get(username=user_name)
                valid = user_a.groups.filter(name="disable").exists()

                if not valid:
                    login(request, user_a)
                    return render(request, "home/main.html", {})

                else:
                    msg = "The User is waiting for admin approval"
                    return render(request, "accounts/login.html", {"form":form, "msg":msg})

            else:
                return redirect("/register")

    else:
        return render(request, "accounts/login.html", {"form":form, "msg":msg})




def register_user(request):

    msg = None
    form = SignUpForm(request.POST)
    letter = ('t', 's', 'o', 'h')
    username = request.POST.get("username")
    if request.method == "POST":
        if len(username) == 8 and username.startswith(letter):
            if User.objects.filter(username=username).exists():
                msg = " The user already exists"
            else:
                user = User(username=username)
                user.save()
                disable_group = Group.objects.get(name='disable')
                disable_group.user_set.add(user)
                
        else:
            msg = "In valid user"

    return render(request, "accounts/register.html", {"form":form, "msg": msg})

