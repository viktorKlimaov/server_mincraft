from audioop import reverse
from unicodedata import category

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название продукта')

    description = models.TextField(max_length=150, verbose_name='описание продукта')

    image = models.ImageField(upload_to='photo/product', blank=True, null=True,
                              verbose_name='Фото')

    category_id = models.ForeignKey(to='Category', on_delete=models.SET_NULL,
                                    verbose_name='категория', blank=True, null=True)

    price = models.IntegerField(verbose_name='стоимость продукта')
    created_at = models.DateField(blank=True, null=True, verbose_name='дата публикации')
    updated_at = models.DateField(blank=True, null=True, verbose_name='дата последнего изменения')


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


    def __str__(self):
        return f'{self.name}'

    # def get_absolute_url(self):
    #     return reverse('mainapp:subject_list', args=[self.name])





class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='название катигории')
    slug = models.CharField( max_length=100, verbose_name='slug', blank=True, null=True,)
    description = models.TextField(max_length=150, verbose_name='описание катигории')

    class Meta:
        verbose_name = 'катигория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'катигории'  # Настройка для наименования набора объектов

    # def get_absolute_url(self):
    #     return reverse('mainapp:subject_list', kwargs={'category': self.pk})

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'








