from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    author = models.ForeignKey('auth.User', verbose_name='Автор', on_delete=models.CASCADE,)
    body = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'