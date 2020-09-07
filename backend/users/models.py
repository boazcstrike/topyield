from django.db import models
from django.contrib.auth.models import AbstractUser

from base.models import CompleteInfo

class User(AbstractUser):
    created_by = models.Foreign(
        'self', on_delete=models.PROTECT, null=True, blank=True)
    updated_at = models.DateTimeField(
        auto_now=True, auto_now_add=False, null=True, blank=True)
    updated_by = models.Foreign(
        'self', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

class Employee(CompleteInfo):
    user = models.OneToOneField('User', on_delete=models.SET_NULL)
    emp_num = models.CharField(max_length=50, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    contact_num = models.CharField(max_length=20, null=True, blank=True)
    em_contact_num = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class Merchant(CompleteInfo):
    name = models.CharField(max_length=255, unique=True)
    company = models.CharField(max_length=255)
    contact_num = models.CharField(max_length=20, null=True, blank=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    sku = models.ManyToManyField("inventory.Sku")