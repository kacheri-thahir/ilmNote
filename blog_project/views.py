from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog,About,Socialmedia_links


def home(request):
    featured_posts=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published')


    context={
        'featured_posts' : featured_posts,
        'posts' : posts,
    }
    return render(request,'home.html',context)


def about(request):
    try:
        about=About.objects.get()
    except:
        about=None

    social_links = Socialmedia_links.objects.all()

    context={
        'about': about,
        'social_links':social_links
    }

    return render(request,'about.html',context)