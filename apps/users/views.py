from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, authenticate
from apps.settings.models import Setting
from django.http import HttpResponse
# Create your views here.

def user_register(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting': setting,
    }
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            user = User.objects.create(username=username, first_name=first_name,
                                       last_name=last_name, email=email)
            user.set_password(password)
            user.save()
            return redirect('user_login')
    return render(request, 'registration.html', context)


def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        except:
            return HttpResponse("Пользователь не найден или пароль не верный")
    context = {
        'setting': setting,
    }
    return render(request, 'sign-in.html', context)


def account(request, username):
    setting = Setting.objects.latest('id')
    user = User.objects.get(username=username)
    context = {
        'user': user,
        'setting': setting,
    }
    return render(request, 'profile.html', context)
