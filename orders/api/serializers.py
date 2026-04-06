from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'product_name', 'customer', 'status', 'created_at']
        read_only_fields = ['id', 'created_at', 'product_name']