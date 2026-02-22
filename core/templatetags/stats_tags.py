from django import template

from customers.models import Customer
from orders.models import Order
from products.models import Product


register = template.Library()

@register.simple_tag
def total_products():
    return Product.objects.count()

@register.simple_tag
def total_customers():
    return Customer.objects.count()

@register.simple_tag
def total_orders():
    return Order.objects.count()
