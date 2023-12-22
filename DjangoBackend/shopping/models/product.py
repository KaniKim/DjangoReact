from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)

    class Meta:
        app_label = "shopping"
