from django import forms    
from .models import Transaction, Category

class TransactionForm(forms.ModelForm):
           class Meta:
               model = Transaction
               fields = ['amount', 'date', 'description', 'category']
               widgets = {
                   'date': forms.DateInput(attrs={'type': 'date'}),
               }