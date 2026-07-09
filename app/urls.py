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
    path('accounts/',include('django.contrib.auth.urls')),
    path('dashboard/',views.dashboard,name='dashboard'),
    
    path("add_category/", views.add_category, name="add_category"),
    path("update_category/<int:id>/", views.update_category, name="update_category"),
    path("delete_category/<int:id>/", views.delete_category, name="delete_category"),

    path("add_post/", views.add_post, name="add_post"),
    path("update_post/<int:id>/", views.update_post, name="update_post"),
    path("delete_post/<int:id>/", views.delete_post, name="delete_post"),

    path("update_user/<int:id>/", views.update_user, name="update_user"),
    path("delete_user/<int:id>/", views.delete_user, name="delete_user"),

    path('add_post',views.add_post,name='add_post'),
    path('add_user/<int:id>',views.add_user,name='add_user')


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )