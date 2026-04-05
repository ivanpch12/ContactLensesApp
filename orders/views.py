from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from accounts.utils import is_manager, is_customer
from orders.forms import OrderCreateForm, OrderEditForm
from orders.models import Order


class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/order-create-edit.html'
    success_url = reverse_lazy('orders:list')

    def test_func(self):
        return is_manager(self.request.user) or is_customer(self.request.user)


class OrderEditView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['status', 'product']
    template_name = 'orders/order-create-edit.html'

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        user = request.user

        if user.groups.filter(name__in=['Manager', 'Employee']).exists():
            return super().dispatch(request, *args, **kwargs)

        if user.groups.filter(name='Customer').exists():
            if order.customer.user == user:
                return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'orders/order-delete.html'
    success_url = reverse_lazy('orders:list')

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if user.groups.filter(name__in=['Manager', 'Employee']).exists():
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order-list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name__in=['Manager', 'Employee']).exists():
            return Order.objects.all()
        elif user.groups.filter(name='Customer').exists():
            return Order.objects.filter(customer__user=user)
        else:
            return Order.objects.none()


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order-detail.html'
    context_object_name = 'order'