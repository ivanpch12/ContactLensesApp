from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from customers.forms import CustomerCreateForm, CustomerEditForm, CustomerDeleteForm
from customers.models import Customer


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = 'customers/customer-create-edit.html'
    success_url = reverse_lazy('customers:list')


class CustomerEditView(UpdateView):
    model = Customer
    form_class = CustomerEditForm
    template_name = 'customers/customer-create-edit.html'
    success_url = reverse_lazy('customers:list')


class CustomerDeleteView(DeleteView):
    model = Customer
    form_class = CustomerDeleteForm
    template_name = 'customers/customer-delete.html'
    success_url = reverse_lazy('customers:list')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer-list.html'
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer-detail.html'
    context_object_name = 'customer'