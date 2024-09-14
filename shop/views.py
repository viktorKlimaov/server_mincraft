from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from mainapp.models import Product, Category
from shop.forms import CategoryForm, ProductForm


class SubjectListView(ListView):
    """
    Контроллер отображения Магазина
    """
    context_object_name = 'Subjects'  # по умолчанию object_list
    model = Product  # queryset = Product.objects.all() можно тоже использовать
    template_name = 'shop/shop_list.html'


    def get_queryset(self, *args, **kwargs):
        try:
            self.category = get_object_or_404(Category, pk=self.kwargs["pk"])
            return Product.objects.filter(category=self.category)
        except KeyError:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["category"] = Category.objects.all()
        return context

#####################################################

class CategoryDetailView(DetailView):
    """
    Контроллер для отображения одной статьи
    """
    model = Category
    template_name = 'shop/shop_category_detail.html'

#############################################################

class SubjectUpdateView(UpdateView):
    """
    Контроллер для обновления статьи
    """
    template_name = 'shop/shop_category_form.html'
    model = Category
    form_class = CategoryForm


    def get_success_url(self):
        return reverse('shop:subject_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     SubjectFormset = inlineformset_factory(Category, Product, form=ProductForm, extra=1)
    #     context_data['formset'] = SubjectFormset
    #     return context_data
###################################################################

class ProductUpdateView(UpdateView):
    """
    Контроллер для обновления статьи
    """
    template_name = 'shop/shop_product_form.html'
    model = Product
    fields = ('name', 'slug', 'description', 'image', 'category',
              'price', 'created_at', 'updated_at')


    def get_success_url(self):
        return reverse('shop:subject_list')

#####################################################
