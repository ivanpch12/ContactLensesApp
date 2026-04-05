from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from products.models import Product
from reviews.forms import ReviewCreateForm, ReviewEditForm, ReviewDeleteForm
from reviews.models import Review


class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'reviews/review-create-edit.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Customer').exists()

    def handle_no_permission(self):
        return redirect('products:list')

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs['product_pk'])
        form.instance.product = product
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.product.get_absolute_url()


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewEditForm
    template_name = 'reviews/review-create-edit.html'

    def get_success_url(self):
        return self.object.product.get_absolute_url()

    def test_func(self):
        review = self.get_object()
        user = self.request.user
        return ((user == review.user and user.groups.filter(name='Customer').exists())
                or self.request.user.groups.filter(name='Manager').exists())


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    form_class = ReviewDeleteForm
    template_name = 'reviews/review-delete.html'

    def test_func(self):
        review = self.get_object()
        user = self.request.user
        return ((self.request.user == review.user and user.groups.filter(name='Customer').exists())
                or self.request.user.groups.filter(name='Manager').exists())

    def get_success_url(self):
        return self.object.product.get_absolute_url()