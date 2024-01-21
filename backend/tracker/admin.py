from django.contrib import admin
from .models import WorldCurrency, Shop, Expense

@admin.register(WorldCurrency)
class WorldCurrencyAdmin(admin.ModelAdmin):
  list_display = ['name', 'symbol', 'code']

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
  list_display = ['name', 'address', 'contact']


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
  list_display = [
    'description',
    'category',
    'shop',
    'currency',
    'total',
    'month',
    'day',
    'year',
    'php',
    'conversion',
    'cell',
  ]

