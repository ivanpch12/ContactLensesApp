from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from orders.api.permissions import OrderPermission
from orders.api.serializers import OrderSerializer
from orders.models import Order
from orders.tasks import send_order_notification_async


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, OrderPermission]

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name__in=['Manager', 'Employee']).exists():
            return Order.objects.select_related('customer', 'product').all()

        if user.groups.filter(name='Customer').exists():
            return Order.objects.select_related('product').filter(customer=user.customer_profile)

        return Order.objects.none()

    def perform_create(self, serializer):
        order = serializer.save(customer=self.request.user.customer_profile)
        try:
            send_order_notification_async(order.id)
        except Exception as e:
            print(f'Failed to send notification: {e}')

        send_order_notification_async(order.id)