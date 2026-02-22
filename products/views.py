from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from products.forms import ProductCreateForm, ProductEditForm, ProductDeleteForm
from products.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/product-create-edit.html'
    success_url = reverse_lazy('products:list')

class ProductEditView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'products/product-create-edit.html'
    success_url = reverse_lazy('products:list')

class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductDeleteForm
    template_name = 'products/product-delete.html'
    success_url = reverse_lazy('products:list')

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)

class ProductListView(ListView):
    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'