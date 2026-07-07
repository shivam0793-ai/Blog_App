from .models import Category,Description,Social

def context_processors_function(request):
    query_set=Category.objects.all()
    Social_link=Social.objects.all()

    try:
        Desc=Description.objects.get()
    except:
        Desc=None

    context={
        'categories':query_set,
        'Desc':Desc,
        'Social_link':Social_link,
    }
    return context
