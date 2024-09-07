from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from mainapp.models import Product, Category


class SubjectListView(ListView):
    """
    Контроллер отображения Магазина
    """
    context_object_name = 'Subjects'  # по умолчанию object_list
    model = Product  # queryset = Product.objects.all() можно тоже использовать
    template_name = 'shop/shop_list.html'
    # category = None
    #
    # def get_queryset(self):
    #     self.category = get_object_or_404(Category, name=self.kwargs["category"])
    #     return Product.objects.filter(category_id=self.category)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["category"] = Category.objects.all()
        return context


class CategoryDetailView(DetailView):
    """
    Контроллер для отображения одной статьи
    """
    model = Category
    template_name = 'shop/shop_category_detail.html'


class SubjectUpdateView(UpdateView):
    """
    Контроллер для обновления статьи
    """
    template_name = 'shop/shop_category_form.html'
    model = Category
    fields = ('name', 'slug', 'description')

    def get_success_url(self):
        return reverse('shop:subject_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)
