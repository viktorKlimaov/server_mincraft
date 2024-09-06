from django.shortcuts import render



class SubjectListView(ListView):
    """
    Контроллер отображения Магазина
    """
    context_object_name = 'Subjects'             # по умолчанию object_list
    model = Product                              # queryset = Product.objects.all() можно тоже использовать
    template_name = 'mainapp/subject_list.html'


    # def get_queryset(self):
    #     self.category = get_object_or_404(Category, pk=self.kwargs["category"])
    #     return Product.objects.filter(category_id=self.category)


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["category"] = Category.objects.all()
        return context

# class CategoryListView(ListView):
#     """
#     Контроллер отображения категорий товара
#     """
#     model = Category
#     template_name = 'includes/inc_nav.html'



class SubjectUpdateView(UpdateView):
    """
    Контроллер для обновления статьи
    """
    template_name = 'mainapp/category_form.html'
    model = Category
    fields = ('name', 'slug', 'description')
    success_url = reverse_lazy('mainapp:subject_list')