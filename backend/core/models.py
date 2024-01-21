from django.db import models
from django.conf import settings


class CreatedInfo(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        settings.USER_AUTH_MODEL,
        on_delete=models.CASCADE,
        related_name="+",)

    class Meta:
        ordering = ['-created_at']
        abstract = True


class UpdatedInfo(CreatedInfo):
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_by = models.ForeignKey(
        settings.USER_AUTH_MODEL,
        on_delete=models.CASCADE,
        related_name="+",)

    class Meta:
        abstract = True


class CancelledInfo(UpdatedInfo):
    cancelled = models.BooleanField(default=False)
    cancelled_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    cancelled_by = models.ForeignKey(
        settings.USER_AUTH_MODEL,
        on_delete=models.CASCADE,
        related_name="+",)

    class Meta:
        abstract = True


class CompleteInfo(UpdatedInfo):
    deactivated = models.BooleanField(default=False)
    deactivated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    deactivated_by = models.ForeignKey(
        settings.USER_AUTH_MODEL,
        on_delete=models.CASCADE,
        related_name="+",)

    class Meta:
        abstract = True


class WorldCurrency(CompleteInfo):
    name = models.CharField(max_length=255, unique=True)
    symbol = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.symbol + self.name