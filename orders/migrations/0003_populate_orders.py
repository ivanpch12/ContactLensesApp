from django.db import migrations

def create_initial_orders(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')
    Product = apps.get_model('products', 'Product')
    Order = apps.get_model('orders', 'Order')

    customers = list(Customer.objects.all())
    products = list(Product.objects.all())

    if not customers or not products:
        return

    orders_data = [
        {'customer': customers[0], 'products': [products[0], products[1]], 'status': 'Pending'},
        {'customer': customers[1], 'products': [products[2]], 'status': 'Shipped'},
        {'customer': customers[2], 'products': [products[3], products[4], products[5]], 'status': 'Delivered'},
        {'customer': customers[3], 'products': [products[6]], 'status': 'Canceled'},
        {'customer': customers[4], 'products': [products[7], products[8]], 'status': 'Pending'},
    ]

    for order_data in orders_data:
        products_list = order_data.pop('products')
        order = Order.objects.create(**order_data)
        order.product.set(products_list)
        order.save()

def delete_initial_orders(apps, schema_editor):
    Order = apps.get_model('orders', 'Order')
    Order.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_options_remove_order_order_date_and_more'),
        ('products', '0003_populate_products'),
        ('customers', '0003_populate_customers'),
    ]

    operations = [
        migrations.RunPython(create_initial_orders, delete_initial_orders),
    ]