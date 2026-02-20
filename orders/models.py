from django.db import models

from customers.models import Customer
from products.models import Product


class Order(models.Model):

    class OrderStatus(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        SHIPPED = 'Shipped', 'Shipped'
        DELIVERED = 'Delivered', 'Delivered'
        CANCELED = 'Canceled', 'Canceled'

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders',
    )

    product = models.ManyToManyField(
        Product,
        related_name='orders',
    )

    status = models.CharField(
        max_length=10,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Order {self.id} for {self.customer}'