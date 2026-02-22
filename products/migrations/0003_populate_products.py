from django.db import migrations
from decimal import Decimal

def create_initial_products(apps, schema_editor):
    Product = apps.get_model('products', 'Product')

    initial_products = [
        # Cooper Vision
        {'name': 'Biofinity', 'product_type': 'Soft', 'price': Decimal('45.00'),
         'description': 'Monthly silicone hydrogel lenses by Cooper Vision.'},
        {'name': 'Clariti 1 Day', 'product_type': 'Soft', 'price': Decimal('35.00'),
         'description': 'Daily disposable lenses by Cooper Vision.'},
        {'name': 'Proclear', 'product_type': 'Soft', 'price': Decimal('50.00'),
         'description': 'Monthly lenses for comfort and hydration.'},
        {'name': 'Avaira Vitality', 'product_type': 'Soft', 'price': Decimal('47.00'),
         'description': 'Monthly lenses for healthy eyes by Cooper Vision.'},
        {'name': 'MyDay', 'product_type': 'Soft', 'price': Decimal('52.00'),
         'description': 'Daily disposable lenses with high oxygen permeability.'},

        # Alcon
        {'name': 'Air Optix Aqua', 'product_type': 'Soft', 'price': Decimal('48.00'),
         'description': 'Monthly lenses by Alcon for clear vision.'},
        {'name': 'Dailies Total1', 'product_type': 'Soft', 'price': Decimal('55.00'),
         'description': 'Daily disposable lenses with water gradient by Alcon.'},
        {'name': 'FreshLook ColorBlends', 'product_type': 'Soft', 'price': Decimal('40.00'),
         'description': 'Colored lenses by Alcon for changing eye color.'},
        {'name': 'Air Optix Night & Day', 'product_type': 'Soft', 'price': Decimal('60.00'),
         'description': 'Monthly extended-wear lenses by Alcon.'},
        {'name': 'Dailies AquaComfort Plus', 'product_type': 'Soft', 'price': Decimal('38.00'),
         'description': 'Daily disposable lenses by Alcon with extra comfort.'},

        # Допълнителни популярни модели
        {'name': 'Biofinity Toric', 'product_type': 'Soft', 'price': Decimal('55.00'),
         'description': 'Toric lenses for astigmatism by Cooper Vision.'},
        {'name': 'Clariti 1 Day Toric', 'product_type': 'Soft', 'price': Decimal('40.00'),
         'description': 'Daily toric lenses by Cooper Vision.'},
        {'name': 'Proclear Toric', 'product_type': 'Soft', 'price': Decimal('53.00'),
         'description': 'Toric monthly lenses for astigmatism.'},
        {'name': 'Air Optix Colors', 'product_type': 'Soft', 'price': Decimal('45.00'),
         'description': 'Colored lenses by Alcon.'},
        {'name': 'Dailies Total1 Multifocal', 'product_type': 'Soft', 'price': Decimal('60.00'),
         'description': 'Daily multifocal lenses by Alcon for presbyopia.'},
    ]

    for product_data in initial_products:
        Product.objects.create(**product_data)


def delete_initial_products(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    names = [
        'Biofinity', 'Clariti 1 Day', 'Proclear', 'Avaira Vitality', 'MyDay',
        'Air Optix Aqua', 'Dailies Total1', 'FreshLook ColorBlends', 'Air Optix Night & Day',
        'Dailies AquaComfort Plus', 'Biofinity Toric', 'Clariti 1 Day Toric', 'Proclear Toric',
        'Air Optix Colors', 'Dailies Total1 Multifocal'
    ]
    Product.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_price'),
    ]

    operations = [
        migrations.RunPython(create_initial_products, delete_initial_products),
    ]