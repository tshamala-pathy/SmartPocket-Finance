from django.shortcuts import render
from .models import Transaction

# Create your views here.
# Views for the Finance app

def home(request):
    transactions = Transaction.objects.all().order_by('-date')
    total_income = sum(t.amount for t in transactions if t.category == 'income')
    total_expense = sum(t.amount for t in transactions if t.category == 'expense')
    balance = total_income - total_expense

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'finance/home.html', context)
