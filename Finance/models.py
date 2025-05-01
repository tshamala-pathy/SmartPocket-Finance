from django.db import models
from django.utils import timezone

# Create your models here.

# Define transaction categories
CATEGORY_CHOICES = [
    ('income', 'Income'),
    ('expense', 'Expense'),
    ('savings', 'Savings'),
]

# Define payment methods
PAYMENT_METHOD_CHOICES = [
    ('cash', 'Cash'),
    ('bank', 'Bank Transfer'),
    ('card', 'Credit/Debit Card'),
    ('mobile', 'Mobile Money'),
    ('other', 'Other'),
]

class Transaction(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='cash')
    vendor = models.CharField(max_length=100, blank=True, help_text="Who or where the transaction was made")
    recurring = models.BooleanField(default=False, help_text="Mark if this is a recurring transaction")
    notes = models.TextField(blank=True, help_text="Additional notes or reminders (optional)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.amount} ({self.category})"

    class Meta:
        ordering = ['-date']
