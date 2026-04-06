from django.urls import path
from reviews.views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView


app_name = 'reviews'

urlpatterns = [
    path('create/<int:product_pk>/', ReviewCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete'),
]