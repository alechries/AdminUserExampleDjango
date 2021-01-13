from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=15)
    author = models.ForeignKey('auth.User', verbose_name='Автор', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE, null=True,)
    body_preview = models.TextField(verbose_name='Превью содержания', null=True, max_length=120)
    body = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='posts_photo', verbose_name='Изображение', null=True)
    pub_date = models.DateTimeField(verbose_name='Дата публикации', null=True)

    def __str__(self):
        return f"{self.title} - {self.body_preview}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'