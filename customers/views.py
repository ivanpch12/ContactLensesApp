from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from accounts.utils import is_manager
from customers.forms import CustomerCreateForm, CustomerEditForm, CustomerDeleteForm
from customers.models import Customer


class CustomerCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = 'customers/customer-create-edit.html'
    success_url = reverse_lazy('customers:list')

    def test_func(self):
        return is_manager(self.request.user)


class CustomerEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Customer
    form_class = CustomerEditForm
    template_name = 'customers/customer-create-edit.html'
    success_url = reverse_lazy('customers:list')

    def test_func(self):
        return is_manager(self.request.user)


class CustomerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Customer
    template_name = 'customers/customer-delete.html'
    success_url = reverse_lazy('customers:list')

    def test_func(self):
        return is_manager(self.request.user)


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer-list.html'
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer-detail.html'
    context_object_name = 'customer'


class CustomerProfileView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'phone', 'address']
    template_name = 'customers/profile.html'

    def get_object(self, queryset=None):
        obj, created = Customer.objects.get_or_create(
            user=self.request.user,
            defaults={
                'first_name': '',
                'last_name': '',
                'email': self.request.user.email or '',
            }
        )

    def get_success_url(self):
        return reverse_lazy('customers:profile')