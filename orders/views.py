from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from orders.forms import OrderFullForm, OrderCustomerForm, OrderCreateFullForm, \
    OrderCreateCustomerForm
from orders.models import Order


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'orders/order-create-edit.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.groups.filter(name__in=['Manager', 'Employee']).exists() or user.groups.filter(name='Customer').exists():
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

    def get_form_class(self):
        user = self.request.user
        if user.groups.filter(name__in=['Manager', 'Employee']).exists():
            return OrderCreateFullForm
        elif user.groups.filter(name='Customer').exists():
            return OrderCreateCustomerForm
        return OrderCreateFullForm

    def form_valid(self, form):
        if self.request.user.groups.filter(name='Customer').exists():
            form.instance.customer = self.request.user.customer_profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('orders:list')


class OrderEditView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'orders/order-create-edit.html'

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        user = request.user

        if user.groups.filter(name__in=['Manager', 'Employee']).exists():
            return super().dispatch(request, *args, **kwargs)
        if user.groups.filter(name='Customer').exists() and order.customer.user == user:
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied

    def get_form_class(self):
        user = self.request.user

        if user.groups.filter(name__in=['Manager', 'Employee']).exists():
            return OrderFullForm
        if user.groups.filter(name='Customer').exists():
            return OrderCustomerForm
        return OrderFullForm


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