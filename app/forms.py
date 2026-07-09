from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category,Blog
from django import forms

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


    def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)
     for field in self.fields.values():
        field.help_text = None


class Category_form(forms.ModelForm):
   class Meta:
      model=Category
      fields=['category_name']


class Blog_form(forms.ModelForm):
   class Meta:
      model=Blog
      exclude=('slug','author')




class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        ]