from django.urls import path
from products.views import ProductCreateView, ProductEditView, ProductDeleteView, ProductListView

app_name = 'products'

urlpatterns = [
    path('products', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('products/<int:pk>/edit/', ProductEditView.as_view(), name='edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
]