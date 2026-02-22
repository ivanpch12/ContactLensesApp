from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from orders.forms import OrderCreateForm, OrderEditForm, OrderDeleteForm
from orders.models import Order


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/order-create-edit.html'
    success_url = reverse_lazy('orders:list')


class OrderEditView(UpdateView):
    model = Order
    form_class = OrderEditForm
    template_name = 'orders/order-create-edit.html'
    success_url = reverse_lazy('orders:list')


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders/order-delete.html'
    success_url = reverse_lazy('orders:list')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order-list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order-detail.html'
    context_object_name = 'order'