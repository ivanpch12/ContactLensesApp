from rest_framework import routers

from orders.api.views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls