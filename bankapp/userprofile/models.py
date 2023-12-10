from django.db import models


class Transaction(models.Model):
    user_email = models.EmailField()
    date_of_transaction = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user_email} - {self.amount} - {self.date_of_transaction}"