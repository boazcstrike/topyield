from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.utils.translation import gettext_lazy as _


from core.models import CompleteInfo


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
    )


class Employee(CompleteInfo):
    user = models.OneToOneField(
        settings.USER_AUTH_MODEL,
        on_delete=models.SET_NULL,
        null=True)
    emp_num = models.CharField(max_length=50, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    contact_num = models.CharField(max_length=20, null=True, blank=True)
    emergency_contact_num = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class Merchant(CompleteInfo):
    name = models.CharField(max_length=255, unique=True)
    company = models.CharField(max_length=255)
    contact_num = models.CharField(max_length=20, null=True, blank=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
