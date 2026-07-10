from rest_framework.serializers import ModelSerializer
from app.models import Blog,Category,Comment,Description

class Blog_serializer(ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'


class category_serializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

        


class comment_serializer(ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'


class Desc_serializer(ModelSerializer):
    class Meta:
        model=Description
        fields='__all__'
