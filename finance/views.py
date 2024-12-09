from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm

@login_required
def transaction_list(request):
    """Display and handle the list of transactions."""
    transactions = Transaction.objects.filter(user=request.user)  
    form = TransactionForm(request.POST or None)
    
    if form.is_valid():
        transaction = form.save(commit=False)
        transaction.user = request.user  
        transaction.save()
        return redirect('transaction_list')  
    balance = get_balance(request)
    
    return render(request, 'finance/transaction_list.html', {
        'form': form, 
        'transactions': transactions, 
        'balance': balance,
    })

def get_balance(request):
    """Calculate the total balance for the logged-in user."""
    if not request.user.is_authenticated:
        return 0  
    income = Transaction.objects.filter(user=request.user, category__name="Income")
    expenses = Transaction.objects.filter(user=request.user, category__name="Expense")

    
    total_income = sum(item.amount for item in income)
    total_expenses = sum(item.amount for item in expenses)
    return total_income - total_expenses
