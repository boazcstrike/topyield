from django.db import models

from core.models import (
  Category,
  UpdatedInfo,
)


class WorldCurrency(UpdatedInfo):
  # currency['country_name'] + ' ' + currency['currency_english_name']
  name = models.CharField(max_length=255, unique=True)
  symbol = models.CharField(max_length=255)
  code = models.CharField(max_length=255, unique=True)

  def __str__(self):
      return f'{self.symbol} {self.name} {self.code}'


class Shop(UpdatedInfo):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255, blank=True, null=True)
  contact = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return self.name


class Expense(UpdatedInfo):
  description = models.CharField(max_length=255, null=True, blank=True)
  category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    related_name='expense_category',
    )
  shop = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    related_name='expense_shop',
    )
  currency = models.ForeignKey(
    WorldCurrency,
    on_delete=models.PROTECT,
    related_name='expense_currency',
    )
  total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  month = models.IntegerField(blank=True, null=True)
  day = models.IntegerField(blank=True, null=True)
  year = models.IntegerField(blank=True, null=True)
  php = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  conversion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  cell = models.CharField(max_length=255)

  def __str__(self):
    return str(self.php)
