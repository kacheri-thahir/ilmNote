from django import forms
from blogs .models import Category,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'


# Blogs Form

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','category','featured_image','short_description','blog_body','status','is_featured')

# New User Creation Form

class AddUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user', None)  # pass current user when initializing
        super().__init__(*args, **kwargs)

        # If current user is not superuser, hide superuser-only fields
        if self.request_user and not self.request_user.is_superuser:
            for field in ['is_superuser', 'groups', 'user_permissions', 'is_staff']:
                self.fields.pop(field, None)


# EditUserForm
class EditUserForm(forms.ModelForm):        #why this when we have AddUserForm why cant we use? Answer is: UserCreationForm comes with password field which is mandatory field to fill but giving permission to manager or others to edit password of the user is not correct password only set or edit by user only so for that purpose we create another modelform to avoid password field 
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user', None)  # pass current user when initializing
        super().__init__(*args, **kwargs)

        # If current user is not superuser, hide superuser-only fields
        if self.request_user and not self.request_user.is_superuser:
            for field in ['is_superuser', 'groups', 'user_permissions', 'is_staff']:
                self.fields.pop(field, None)