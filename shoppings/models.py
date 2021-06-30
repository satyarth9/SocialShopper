from django.db import models

from accounts.models import AppUser


class Shopping(models.Model):
    PROPOSED = 'PR'
    ACTIVE = 'AC'
    COMPLETED = 'CO'
    shopping_status_choices = (
        (PROPOSED, 'Proposed'),
        (ACTIVE, 'Active'),
        (COMPLETED, 'Completed')
    )
    shopper = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    shopping_status = models.CharField(max_length=2, choices=shopping_status_choices, default=PROPOSED)
    total_amount = models.FloatField()
    venue = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return f"{self.shopper.name} : {self.venue} : {self.date}"



