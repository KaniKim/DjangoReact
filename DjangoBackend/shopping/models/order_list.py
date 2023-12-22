from django.db import models

from shopping.models.customer import Customer
from shopping.models.product import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    products = models.ManyToManyField(Product, null=True)
    order_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "shopping"
