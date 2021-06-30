from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import JsonResponse


def home(request):
    if request.user.is_authenticated:
        return redirect("user_home")
    else:
        return render(request, "login.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("user_home")
        else:
            return JsonResponse({
                "error": "bad credentials"
            })


def profile(request):
    if request.user.is_authenticated:
        return render(request, "user_profile.html")


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('home')
