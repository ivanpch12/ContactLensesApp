from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from accounts.utils import is_manager
from products.forms import ProductCreateForm, ProductEditForm, ProductDeleteForm
from products.models import Product


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/product-create-edit.html'
    success_url = reverse_lazy('products:list')

    def test_func(self):
        return is_manager(self.request.user)

class ProductEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'products/product-create-edit.html'
    success_url = reverse_lazy('products:list')

    def test_func(self):
        return is_manager(self.request.user)

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/product-delete.html'
    success_url = reverse_lazy('products:list')

    def test_func(self):
        return is_manager(self.request.user)

class ProductListView(ListView):
    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'