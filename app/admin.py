from django.contrib import admin
from .models import Blog, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','created_at','update_at',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'author',
        'status',
        'is_featured',
        'created_at',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    search_fields=('title','category__category_name')
