from django.urls import path
from customers.views import CustomerListView, CustomerCreateView, CustomerDetailView, CustomerEditView, \
    CustomerDeleteView

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='list'),
    path('create/', CustomerCreateView.as_view(), name='create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', CustomerEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete'),
]