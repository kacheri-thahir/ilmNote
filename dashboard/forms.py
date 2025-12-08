from django import forms
from blogs .models import Category,Blog

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