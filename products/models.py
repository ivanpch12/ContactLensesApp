from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg
from django.urls import reverse


class Product(models.Model):
    class LensType(models.TextChoices):
        DAILY = 'Daily', 'Daily'
        WEEKLY = 'Weekly', 'Weekly'
        MONTHLY = 'Monthly', 'Monthly'
        QUARTERLY = 'Quarterly', 'Quarterly'
        HALF_YEARLY = 'Half-Yearly', 'Half-Yearly'
        YEARLY = 'Yearly', 'Yearly'

    name = models.CharField(
        max_length=100,
    )

    lens_type = models.CharField(
        max_length=20,
        choices=LensType.choices,
        default=LensType.MONTHLY,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000)
        ]
    )

    description = models.TextField(
        blank=True,
    )


    def average_rating(self):
        return self.reviews.aggregate(Avg('rating'))['rating__avg']


    def get_edit_url(self):
        return reverse('products:edit', kwargs={'pk': self.pk})


    def get_delete_url(self):
        return reverse('products:delete', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.name