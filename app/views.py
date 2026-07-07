from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Blog
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def Home(request):
    blogs=Blog.objects.filter(is_featured=True)
    categories=Category.objects.all()
    context={
        'blog':blogs,
        'categories':categories
        }
    return render(request,'app/Home.html',context=context)



@login_required
def all_blogs(request,id):
    if id is None:
        query_set=Blog.objects.filter(status='Published').order_by('created_at')
    else:
        query_set=Blog.objects.filter(category=id,status='Published')
    return render(request,'app/all_blogs.html',{'Blog':query_set})

@login_required
def OneBlogDetails(request,slug):
    data= get_object_or_404(Blog,slug=slug,status='Published')
    return render(request,'app/OneBlogDetails.html',{'blog':data})

from django.db.models import Q


@login_required
def Search_view(request):
    keyword = request.GET.get('Keyword', '')

    query_set = Blog.objects.filter(
        Q(title__icontains=keyword) |
        Q(category__category_name__icontains=keyword) |
        Q(author__username__icontains=keyword) |
        Q(short_desc__icontains=keyword) |
        Q(slug__icontains=keyword),
        status='Published'
    )

    return render(request, 'app/all_blogs.html', {'Blog': query_set})


from .forms import RegForm
def regview(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegForm()
    
    return render(request,'app/regform.html',{'form':form})