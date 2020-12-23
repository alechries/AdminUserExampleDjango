from django.db import models


class Example0(models.Model):

    name = models.CharField('Название', max_length=200)
    type = models.TextField('Тип')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f"Example0 {self.name} {self.pub_date}"

    class Meta:
        verbose_name = 'Пример0'
        verbose_name_plural = 'Примеры0'


class Example1(models.Model):

    name = models.CharField('Название', max_length=200)
    type = models.TextField('Тип')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f"Example1 {self.name} {self.pub_date}"

    class Meta:
        verbose_name = 'Пример1'
        verbose_name_plural = 'Примеры1'