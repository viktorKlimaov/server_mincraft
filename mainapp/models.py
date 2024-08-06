from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'  # Настройка для наименования одного объекта
        verbose_name_plural = 'студенты'  # Настройка для наименования набора объектов
