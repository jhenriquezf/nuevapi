from django.db import models

from cuentas.models.base import BaseEntity
from cuentas.models.category import Category


class Product(BaseEntity):
    title = models.CharField(max_length=180)
    description = models.TextField(null=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='product', null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
