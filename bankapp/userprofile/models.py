from django.db import models


class Transaction(models.Model):
    user_email = models.EmailField()
    date_of_transaction = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user_email} - {self.amount} - {self.date_of_transaction}"
    

#     user_email,amount,date_of_transaction
# eva@mail.com, 150.0, 01-09-2023
# adam@mail.com, 75.25, 28-08-2023
# bela@mail.com, 1000, 07-08-2023