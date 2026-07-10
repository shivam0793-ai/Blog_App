from django.urls import path,include
from .views import*
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('blogapiview',blog_view)
router.register('categoryapiview',category_view)
router.register('commentapiview',Comment_view)
router.register('descapiview',Desc_view)


urlpatterns=[
        path("login/", api_login, name="api_login"),
]
urlpatterns+=router.urls