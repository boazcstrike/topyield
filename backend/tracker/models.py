from django.db import models


class Shop(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255, blank=True, null=True)
  contact = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return self.name


class Expense(models.Model):
  description = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  brand_shop = models.CharField(max_length=255)
  currency = models.CharField(max_length=255)
  total = models.DecimalField(max_digits=10, decimal_places=2)
  month = models.IntegerField()
  day = models.IntegerField()
  year = models.IntegerField()
  php = models.DecimalField(max_digits=10, decimal_places=2)
  conversion = models.IntegerField()

  def __str__(self):
    return str(self.php)
