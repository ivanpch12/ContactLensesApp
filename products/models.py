from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
    )

    product_type = models.CharField(
        max_length=50,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name