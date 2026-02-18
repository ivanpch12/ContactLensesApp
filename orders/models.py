from django.db import models

from customers.models import Customer
from products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )

    product = models.ManyToManyField(
        Product,
    )

    order_date = models.DateField(
        auto_now_add=True,
    )

    status = models.CharField(
        max_length=20,
        default='Pending',
    )

    def __str__(self):
        return f'Order {self.id} for {self.customer}'