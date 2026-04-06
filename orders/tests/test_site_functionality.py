from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Group

from products.models import Product
from orders.models import Order
from reviews.models import Review
from customers.models import Customer


User = get_user_model()

class SiteFunctionalityTests(TestCase):

    def setUp(self):
        self.manager_group, _ = Group.objects.get_or_create(name='Manager')
        self.employee_group, _ = Group.objects.get_or_create(name='Employee')
        self.customer_group, _ = Group.objects.get_or_create(name='Customer')

        self.manager = User.objects.create_user('manager', password='pass')
        self.manager.groups.add(self.manager_group)

        self.employee = User.objects.create_user('employee', password='pass')
        self.employee.groups.add(self.employee_group)

        self.customer_user = User.objects.create_user('customer', password='pass')
        self.customer_user.groups.add(self.customer_group)

        self.customer_profile = Customer.objects.create(
            user=self.customer_user,
            email='customer@example.com'
        )

        self.product = Product.objects.create(name='Lens A', lens_type='Type1', price=100)

        self.client = Client()

    def test_create_order(self):
        order = Order.objects.create(customer=self.customer_profile, status='Pending')

        order.product.add(self.product)

        self.assertEqual(order.customer, self.customer_profile)
        self.assertIn(self.product, order.product.all())
        self.assertEqual(order.status, 'Pending')

    def test_average_rating(self):
        Review.objects.create(product=self.product, user=self.customer_user, rating=4, comment='Good')
        Review.objects.create(product=self.product, user=self.customer_user, rating=5, comment='Excellent')
        avg = self.product.average_rating()
        self.assertEqual(avg, 4.5)

    def test_manager_can_access_product_create(self):
        self.client.login(username='manager', password='pass')
        response = self.client.get(reverse('products:create'))
        self.assertEqual(response.status_code, 200)

    def test_customer_cannot_access_product_create(self):
        self.client.login(username='customer', password='pass')
        response = self.client.get(reverse('products:create'))
        self.assertNotEqual(response.status_code, 200)

    def test_customer_can_access_product_list(self):
        self.client.login(username='customer', password='pass')
        response = self.client.get(reverse('products:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_customer_can_add_review_button_visible(self):
        self.client.login(username='customer', password='pass')
        response = self.client.get(reverse('products:detail', args=[self.product.pk]))
        self.assertContains(response, 'Add Review')

    def test_customer_cannot_edit_other_review(self):
        other_customer = User.objects.create_user('other', password='pass')
        other_customer.groups.add(self.customer_group)
        review = Review.objects.create(product=self.product, user=other_customer, rating=3, comment='Meh')
        self.client.login(username='customer', password='pass')
        response = self.client.get(reverse('reviews:edit', args=[review.pk]))
        self.assertNotEqual(response.status_code, 200)

    def test_customer_can_create_order(self):
        self.client.login(username='customer', password='pass')
        response = self.client.post(reverse('orders:create'), {
            'product': self.product.pk,
            'status': 'Pending'
        })
        self.assertEqual(Order.objects.filter(customer=self.customer_profile).count(), 1)

    def test_employee_can_view_all_orders(self):
        order = Order.objects.create(customer=self.customer_profile, status='Pending')

        order.product.set([self.product])

        self.client.login(username='employee', password='pass')

        response = self.client.get('/orders/')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, f'Order #{order.id}')

        self.assertContains(response, 'Pending')

    def test_customer_can_only_view_own_orders(self):
        other_customer_user = User.objects.create_user('other_customer', password='pass')
        other_customer_user.groups.add(self.customer_group)
        other_profile = Customer.objects.create(user=other_customer_user)

        other_order = Order.objects.create(customer=other_profile, status='Pending')
        other_order.product.set([self.product])  # добавяме продукта към M2M полето

        own_order = Order.objects.create(customer=self.customer_profile, status='Pending')
        own_order.product.set([self.product])

        self.client.login(username='customer', password='pass')

        response = self.client.get(reverse('orders:list'))
        orders = response.context['orders']  # или response.data, ако е API

        self.assertIn(own_order, orders)
        self.assertNotIn(other_order, orders)

    def test_order_creation_triggers_notification_task(self):
        self.client.force_login(self.customer_user)

        data = {
            'status': 'Pending',
            'product': [self.product.id],
        }

        with patch('orders.api.views.send_order_notification_async') as mock_task:
            response = self.client.post(reverse('order-list'), data)

            self.assertEqual(response.status_code, 201)

            order_id = response.json()['id']

            calls = [call_args[0][0] for call_args in mock_task.call_args_list]
            self.assertIn(order_id, calls)

    def test_manager_can_delete_order(self):
        order = Order.objects.create(customer=self.customer_profile, status='Pending')

        order.product.set([self.product])

        self.client.login(username='manager', password='pass')

        response = self.client.post(f'/orders/{order.id}/delete/')

        self.assertEqual(response.status_code, 302)

        self.assertFalse(Order.objects.filter(id=order.id).exists())

    def test_customer_cannot_delete_other_order(self):
        other_customer_user = User.objects.create_user('other_customer2', password='pass')
        other_customer_user.groups.add(self.customer_group)
        other_profile = Customer.objects.create(user=other_customer_user)

        other_order = Order.objects.create(customer=other_profile, status='Pending')
        other_order.product.set([self.product])

        self.client.login(username='customer', password='pass')

        response = self.client.post(reverse('orders:delete', args=[other_order.id]))

        self.assertEqual(response.status_code, 403)