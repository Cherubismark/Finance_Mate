from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            amount = models.DecimalField(max_digits=10, decimal_places=2)
            description = models.TextField()
            date = models.DateField()
            category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
       
            def __str__(self):
               return f'{self.description} - {self.amount}'
       
            def get_balance(self):
               """Method to calculate the user's balance"""
               income = Transaction.objects.filter(user=self.user, category__name="Income")
               expenses = Transaction.objects.filter(user=self.user, category__name="Expense")
               total_income = sum([item.amount for item in income])
               total_expenses = sum([item.amount for item in expenses])
               return total_income - total_expenses