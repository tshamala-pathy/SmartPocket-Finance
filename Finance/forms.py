from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'category', 'payment_method', 'vendor', 'description']
        widgets = {
            'category': forms.Select(choices=Transaction.CATEGORY_CHOICES),
            'payment_method': forms.Select(choices=Transaction.PAYMENT_METHOD_CHOICES),
        }
        labels = {
            'title': 'Transaction Title',
            'amount': 'Transaction Amount',
            'category': 'Transaction Category',
            'payment_method': 'Payment Method',
            'vendor': 'Vendor',
            'description': 'Description (optional)',
        }
        help_texts = {
            'title': 'Enter a brief title for the transaction.',
            'amount': 'Enter the amount of the transaction.',
            'category': 'Select the category for this transaction.',
            'payment_method': 'Select the payment method used.',
            'vendor': 'Enter the vendor or payee name.',
            'description': 'Optional: Enter any additional details about the transaction.',
        }
        error_messages = {
            'title': {
                'max_length': "This title is too long.",
            },
            'amount': {
                'required': "Please enter the transaction amount.",
                'invalid': "Enter a valid number for the amount.",
            },
        }
        