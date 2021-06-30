from django.db import models

from shoppings.models import Shopping
from accounts.models import AppUser


class ShoppingRequest(models.Model):
    REQUESTED = "RE"
    APPROVED = "AP"
    CANCELLED = "CA"
    DENIED = "DE"

    sr_choices = (
        (REQUESTED, "Requested"),
        (APPROVED, "Approved"),
        (CANCELLED, "Cancelled"),
        (DENIED, "Denied")
    )

    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE, related_name="requests")
    requestor = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=2, choices=sr_choices, default=REQUESTED)

    def __str__(self):
        return f"{self.requestor} : {self.shopping.venue} : {self.amount}"


class Item(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    quantity = models.CharField(max_length=10)
    shopping_request = models.ForeignKey(ShoppingRequest, on_delete=models.CASCADE, related_name="items")
    estimated_price = models.FloatField()

    def __str__(self):
        return f"{self.name} : {self.brand} : {self.quantity}"