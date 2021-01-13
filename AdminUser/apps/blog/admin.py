from django.contrib import admin
from .models import Post, Category


class DontLog:
    def log_addition(self, *args):
        return


class PostAdmin(DontLog, admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'pub_date', 'image', 'body_preview')


class CategoryAdmin(DontLog, admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


