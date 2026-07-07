from django.contrib import admin
from .models import Blog, Category,Description,Social
from .forms import RegForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
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


@admin.register(Description)
class DescAdmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        if Description.objects.all().count()<1:
            return True
        return False
