from django.shortcuts import render
from django.urls import reverse_lazy, reverse
# from webapp.form import ProductForm
from webapp.models import Adds, Comments
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class ProductList(ListView):
    template_name = 'product_html_files/index.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 3


class ProductCreate(PermissionRequiredMixin, CreateView):
    template_name = 'product_html_files/product_create.html'
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

class ProductUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'product_html_files/product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

class DeleteProduct(PermissionRequiredMixin, DeleteView):
    template_name = 'product_html_files/product_delete.html'
    model = Product
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'


class ProductView(DetailView):
    template_name = 'product_html_files/product_view.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.all()

        if not self.request.user.has_perm('webapp.view_not_moderated_review'):
            reviews = reviews.filter(is_moderated=True)

        context['reviews'] = reviews.order_by('-edited_at')
        return context