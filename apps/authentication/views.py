# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group

from .models import UserHermes
from .forms import LoginForm, SignUpForm
import os
import datetime

def login_view(request):
    msg = None
    form = LoginForm(request.POST or None)
    
    if request.method == "POST":
        if request.POST.get("login"):
            user_name = request.POST.get("username")
            # current_user = os.getlogin()
            
            user = authenticate(username=user_name, password="@hermes510" if user_name != 'admin' else 'admin')

            if user is not None:
                valid = user.groups.filter(name="disable").exists()

                if not valid:
                    login(request, user)
                    return redirect('/')

                else:
                    msg = "המשתמש מחכה לאישור מנהל"
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
    phone_number = request.POST.get("phone_number")
    office = request.POST.get("office")

    if request.method == "POST":
        if len(username) == 8 and username.startswith(letter) and form.is_valid():
            if User.objects.filter(username=username).exists():
                msg = 'המשתמש קיים במערכת'
            else:
                user = User(username=username, password="@hermes510", date_joined=datetime.date.today())
                user.save()
                huser = UserHermes(user=user,phone_number=phone_number,office=office)
                huser.save()
                disable_group = Group.objects.get(name='disable')
                disable_group.user_set.add(user)
                return redirect('waiting_page')
        else:
            msg = "Invalid user"

    return render(request, "accounts/register.html", {"form":form, "msg": msg})

def waiting_page(request):
    return render(request, "accounts/waiting_page.html")