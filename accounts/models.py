from django.db import models
from django.contrib.auth.models import User


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    society = models.CharField(max_length=30)
    shops_done = models.IntegerField()
    shops_requested = models.IntegerField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} : {self.phone} : {self.email}"
