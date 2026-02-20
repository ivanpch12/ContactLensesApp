from django.urls import path
from orders.views import OrderCreateView, OrderEditView, OrderDeleteView, OrderListView, OrderDetailView

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='list'),
    path('create/', OrderCreateView.as_view(), name='create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', OrderEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='delete'),
]