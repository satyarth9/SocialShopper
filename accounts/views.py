from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")


def login(request):
    return JsonResponse({
        "OK": "Json Working"
    })
