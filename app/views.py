from django.shortcuts import render
from .models import Category,Blog
from django.http import HttpResponse

def Home(request):
    blogs=Blog.objects.filter(is_featured=True)
    categories=Category.objects.all()

    context={
        'blog':blogs,
        'categories':categories
        }
    return render(request,'app/index.html',context=context)

    
def blogs_view(request):
    query_set=Blog.objects.all().order_by('created_at')
    return render(request,'app/blogs_view.html',{'context':query_set})

import json
def category_bolg(request,catid):
    Data=Blog.objects.filter(category=catid)
    context={
        'Blog':Data
    }
    return render(request,'app/completeBlog.html',context)


def blogindetails(request,id):
    data= Blog.objects.get(id=id)
    return render(request,'app/blogindetails.html',{'blog':data})