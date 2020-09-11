from django.db import models
from django.conf import settings

from core.models import CompleteInfo, UpdatedInfo


class Product_Category(CompleteInfo):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='parent category of the category',
        null=True, blank=True)

    class Meta:
        verbose_name = _("Product_Category")
        verbose_name_plural = _("Product_Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_Category_detail", kwargs={"pk": self.pk})


class Product_Tag(UpdatedInfo):
    name = models.CharField(max_length=255, unique=True)
    product = models.ManyToManyField("Product")

    class Meta:
        verbose_name = _("Product_Tag")
        verbose_name_plural = _("Product_Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_Tag_detail", kwargs={"pk": self.pk})


class Product(UpdatedInfo):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    use = models.TextField(null=True, blank=True)
    average_selling_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    average_buying_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    category = models.ManyToManyField("Product_Category")

    def __str__(self):
        return self.name


class UM_Dimensions(UpdatedInfo):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Unit_of_Measurement(UpdatedInfo):
    dimension = models.ForeignKey('UM_Dimensions', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Sku_Brand(UpdatedInfo):
    name = models.CharField(max_length=255, unique=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Sku(CompleteInfo):
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    brand = models.ForeignKey('Sku_Brand', on_delete=models.PROTECT)
    sell_price = models.DecimalField(max_digits=12, decimal_places=2)
    buying_price = models.DecimalField(max_digits=12, decimal_places=2)
    in_stock = models.DecimalField(max_digits=12, decimal_places=5)
    unit_of_measurement = models.ForeignKey(
        'Unit_of_Measurement', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Sku_sell_log(models.Model):
    sku = models.ForeignKey('Sku', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.sku.name


class Sku_buy_log(models.Model):
    sku = models.ForeignKey('Sku', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.sku.name


class sku_details(UpdatedInfo):
    sku = models.ForeignKey('Sku', on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=12, decimal_places=5)
    height_um = models.ForeignKey(
        'Unit_of_Measurement', on_delete=SET_NULL, null=True)
    width = models.DecimalField(max_digits=12, decimal_places=5)
    width_um = models.ForeignKey(
        'Unit_of_Measurement', on_delete=SET_NULL, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=5)
    weight_um = models.ForeignKey(
        'Unit_of_Measurement', on_delete=SET_NULL, null=True)
    extra_info = models.JSONField()

    def __str__(self):
        return self.sku.name


class Shipment(CancelledInfo):
    supplier = models.ForeignKey('users.Merchant', on_delete=models.PROTECT)
    ref_num = models.CharField(max_length=255)
    arrived_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    released_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.ref_num
