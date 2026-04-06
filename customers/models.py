from django.conf import settings
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer_profile',
        null=True,
        blank=True,
    )

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        unique=True,
    )

    phone = models.CharField(
        max_length=20,
    )

    address = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


    def get_edit_url(self):
        return reverse('customers:edit', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('customers:delete', kwargs={'pk': self.id})


    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'