# Generated by Django 3.1.4 on 2021-01-05 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_body_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body_preview',
            field=models.TextField(max_length=100, null=True, verbose_name='Превью содержания'),
        ),
    ]
