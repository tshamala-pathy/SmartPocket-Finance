from django.contrib import admin
from .models import Transaction

# Register your models here.
admin.site.site_header = "SmartPocket Admin"

# Finance/admin.py
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'payment_method', 'vendor', 'date')
    search_fields = ('title', 'vendor', 'category')
    list_filter = ('category', 'payment_method', 'date')
    ordering = ('-date',)
    date_hierarchy = 'date'
    list_per_page = 20