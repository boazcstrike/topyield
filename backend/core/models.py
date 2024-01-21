from django.db import models
from django.conf import settings

from django.contrib.auth.models import User


class CreatedInfo(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,)

    class Meta:
        ordering = ['-created_at']
        abstract = True


class UpdatedInfo(CreatedInfo):
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,)

    class Meta:
        abstract = True


class CancelledInfo(UpdatedInfo):
    cancelled = models.BooleanField(default=False)
    cancelled_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    cancelled_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,)

    class Meta:
        abstract = True


class CompleteInfo(UpdatedInfo):
    deactivated = models.BooleanField(default=False)
    deactivated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    deactivated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,)

    class Meta:
        abstract = True



class Category(UpdatedInfo):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
