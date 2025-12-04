from django.shortcuts import render,redirect,get_object_or_404
from . models import Blog,Category
from django.db.models import Q
# Create your views here.

def posts_by_category(request,category_id):
    posts=Blog.objects.filter(status='Published',category=category_id)
    # To get Category Name in posts_by_category.html
    try:
        category=Category.objects.get(pk=category_id) #when ever we use get method use try and except block (if we want to do custom actions means if the category doesnt exist here redirect to home for those purpose use try and except block , if we wan to show 404 page to user use method get_object_or_404 method)
    except:
        return redirect('home')
    
    # category=get_object_or_404(Category, pk = category_id)
    
    context={
        'posts' : posts,
        'category' : category,
    }

    return render(request,'posts_by_category.html',context)


# for each blog

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug,status='Published')
    context={
        'single_blog' : single_blog
    }
    return render(request,'blogs.html',context)


# search bar views

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status='Published')

    context={
        'blogs' : blogs,
        'keyword' : keyword,
    }
    return render(request,'search.html',context)