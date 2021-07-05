from django.shortcuts import render, get_object_or_404

from .models import Shopping
from shop_requests.models import Item


def user_home(request, status="pr"):
    shoppings = Shopping.objects.all().filter(
     shopping_status=status.upper()
    )
    context = {
        "shoppings": shoppings
    }
    if request.user.is_authenticated:
        return render(request, "user_home.html", context)


def shopping_detail(request, shopping_id):
    if request.method == "POST":
        shopping = get_object_or_404(Shopping, pk=shopping_id)
        context = {"shopping" : shopping}
        return render(request, "shopping_detail.html", context)

