from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Blog,Comment
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from .forms import Category_form
from django.db.models import Q


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
     if request.method=='POST':
         comment=Comment()
         comment.slug=slug
         comment.user=request.user
         comment.comment=request.POST.get('comment')
         comment.save()
         return HttpResponseRedirect(request.path_info)
     else:
         data= get_object_or_404(Blog,slug=slug,status='Published')
         comment=Comment.objects.filter(slug=slug)
         context={
             'blog':data,
             'comment':comment
         }
     return render(request,'app/OneBlogDetails.html',context)




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


def access():
    context = {
    "total_categories": Category.objects.count(),
    "total_posts": Blog.objects.count(),
    "categories": Category.objects.all(),
    "posts": Blog.objects.select_related("category"),
    "users": User.objects.all(),
    'Category_form':Category_form()
    }
    return context


def is_staff_user(user):
    return user.is_staff

@user_passes_test(is_staff_user)
def dashboard(request):
    context =access()
    return render(request, "app/dashboard.html", context)    



def add_category(request):
    if request.method == "POST":
        form = Category_form(request.POST)
        if form.is_valid():
            form.save()

    return redirect("dashboard")


def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.category_name = request.POST.get("update_category")
        category.save()
    return redirect("dashboard")


def delete_category(request, id):
    if request.method == "POST":
        category = get_object_or_404(Category, id=id)
        category.delete()
    return redirect("dashboard")



def add_post(request):
    if request.method == "POST":
        pass
    return redirect("dashboard")


def update_post(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        # Example
        post.title = request.POST.get("title")
        post.save()
    return redirect("dashboard")


def delete_post(request, id):
    if request.method == "POST":
        post = get_object_or_404(Blog, id=id)
        post.delete()
    return redirect("dashboard")



def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.username=request.POST.get('username')
        user.email = request.POST.get("email")
        user.save()
    return redirect("dashboard")


def delete_user(request, id):
    if request.method == "POST":
        user = get_object_or_404(User, id=id)
        user.delete()
    return HttpResponseRedirect("dashboard")



from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from .forms import Blog_form

def add_post(request):
    if request.method == "POST":
        form = Blog_form(request.POST, request.FILES)
        if form.is_valid():

            blog = form.save(commit=False)
            blog.author = request.user
            blog.slug = slugify(blog.title)
            blog.save()

            blog.slug = f"{slugify(blog.title)}-{blog.id}"
            blog.save(update_fields=["slug"])
            return redirect("dashboard")

    else:
        form = Blog_form()

    return render(request, "app/addblog.html", {"form": form})



from .forms import AddUserForm

def add_user(request, id):

    if id==0:
        user = None
    else:
        user = get_object_or_404(User, id=id)


    if request.method == "POST":
        form = AddUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = AddUserForm(instance=user)
    return render(request, "app/adduser.html", {
        "form": form,
        'id':id
    })