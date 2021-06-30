from django.shortcuts import render


def user_home(request):
    print("we are here")
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, "user_home.html")