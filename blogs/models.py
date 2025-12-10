from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=60,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Categories'        #in database to make correct spelling

    def __str__(self):
        return self.category_name
    
STATUS_CHOICE = (               #for status dropdown menu
    ("Draft","Draft"),
    ("Published","Published")
)

class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='uploads/%y/%m/%d',blank=True,default='defaults/ilmnote_default_image.jpg')
    short_description=models.TextField(max_length=500)
    blog_body=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICE,default="Draft")
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class About(models.Model):
    about_heading=models.CharField(max_length=25)
    about_description=models.TextField(max_length=1000)
    about_image=models.ImageField(upload_to='about_image')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='About' 

    def __str__(self):
        return self.about_heading


class Socialmedia_links(models.Model):
    platform=models.CharField(max_length=30,null=False)
    link=models.URLField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Socialmedia_links' 

    def __str__(self):
        return self.platform
    

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.TextField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    
    
