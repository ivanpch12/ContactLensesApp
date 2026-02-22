from django.db import migrations

def create_initial_customers(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')

    initial_customers = [
        {'first_name': 'Ivan', 'last_name': 'Chardakov', 'email': 'ivan@example.com', 'phone': '+359888111222', 'address': 'Sofia, Bulgaria'},
        {'first_name': 'Maria', 'last_name': 'Petrova', 'email': 'maria@example.com', 'phone': '+359888333444', 'address': 'Plovdiv, Bulgaria'},
        {'first_name': 'Georgi', 'last_name': 'Ivanov', 'email': 'georgi@example.com', 'phone': '+359888555666', 'address': 'Varna, Bulgaria'},
        {'first_name': 'Elena', 'last_name': 'Dimitrova', 'email': 'elena@example.com', 'phone': '+359888777888', 'address': 'Burgas, Bulgaria'},
        {'first_name': 'Petar', 'last_name': 'Kostov', 'email': 'petar@example.com', 'phone': '+359888999000', 'address': 'Ruse, Bulgaria'},
    ]

    for customer_data in initial_customers:
        Customer.objects.create(**customer_data)

def delete_initial_customers(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')
    emails = [
        'ivan@example.com','maria@example.com','georgi@example.com','elena@example.com','petar@example.com'
    ]
    Customer.objects.filter(email__in=emails).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_options_customer_created_at_and_more'),
    ]

    operations = [
        migrations.RunPython(create_initial_customers, delete_initial_customers),
    ]