from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from .pagination import pagination_page,limitoffset_pagination
from rest_framework.filters import SearchFilter

class blog_view(ModelViewSet):
    serializer_class=Blog_serializer
    queryset=Blog.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    search_fields=['category',]
    


class category_view(ModelViewSet):
    serializer_class=category_serializer
    queryset=Category.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    pagination_class=limitoffset_pagination
    search_fields=['category_name',]


class Desc_view(ModelViewSet):
    serializer_class=Desc_serializer
    queryset=Description.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]


class Comment_view(ModelViewSet):
    serializer_class=comment_serializer
    queryset=Comment.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]





def api_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)

            return render(request, "api/token.html", {
                "token": token.key,
                "user": user
            })

        return render(request, "api/login.html", {
            "error": "Invalid Username or Password"
        })

    return render(request, "api/login.html")