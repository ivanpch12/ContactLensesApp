from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from accounts.utils import is_manager
from orders.forms import OrderCreateForm, OrderEditForm
from orders.models import Order


class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/order-create-edit.html'
    success_url = reverse_lazy('orders:list')

    def test_func(self):
        return is_manager(self.request.user)


class OrderEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderEditForm
    template_name = 'orders/order-create-edit.html'
    success_url = reverse_lazy('orders:list')

    def test_func(self):
        return is_manager(self.request.user)


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    template_name = 'orders/order-delete.html'
    success_url = reverse_lazy('orders:list')

    def test_func(self):
        return is_manager(self.request.user)


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order-list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order-detail.html'
    context_object_name = 'order'