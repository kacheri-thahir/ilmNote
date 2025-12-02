from django.shortcuts import render,redirect,get_object_or_404
from . models import Blog,Category
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
