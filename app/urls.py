from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.Home,name='Home'),
    path('blogs/',views.blogs_view,name='blogs'),
    path('category_bolg/<int:catid>',views.category_bolg,name='category_bolg'),
    path('blogindetails/<int:id>',views.blogindetails,name='blogindetails')
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )