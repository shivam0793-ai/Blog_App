from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.Home,name='Home'),
    path('all_blogs/<int:id>/',views.all_blogs,name='all_blogs'),
    path('OneBlogDetails/<slug:slug>/',views.OneBlogDetails,name='OneBlogDetails'),
    path('Search/posts/',views.Search_view,name='Search'),
    path('reg/',views.regview,name='reg'),
    path('accounts/',include('django.contrib.auth.urls'))

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )