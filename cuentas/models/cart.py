from django.db import models
from cuentas.models.base import BaseEntity
from cuentas.models.product import Product
from django.contrib.auth.models import User


class Cart(BaseEntity):
    products = models.ManyToManyField(Product, null=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)
    datecompleted = models.DateTimeField(null=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.total + '- by' + self.user.username
