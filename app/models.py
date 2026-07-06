from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural='Category'
    



STATUS_CHOICE=(
    ('Published','Published'),
    ('Draft','Draft')
)


class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=120)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='blog_image')
    short_desc=models.TextField(max_length=500)
    blog_body=models.CharField(max_length=1000)
    status=models.CharField(max_length=50,choices=STATUS_CHOICE,default='Draft',blank=True)
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)