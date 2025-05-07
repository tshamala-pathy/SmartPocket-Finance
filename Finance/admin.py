from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date', 'payment_method')
    list_filter = ('category', 'payment_method', 'date')
    search_fields = ('title', 'vendor')
    ordering = ('-date',)
    date_hierarchy = 'date'