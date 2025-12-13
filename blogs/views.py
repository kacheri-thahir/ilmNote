from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from . models import Blog,Category,Comment
from django.db.models import Q
from django.db.models.functions import Replace, Lower
from django.contrib.auth.decorators import login_required

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
    random_categories = Category.objects.order_by('created_at')[:6]     #to display any 6 categories in single blog page
    # Comments
    comments=Comment.objects.filter(blog=single_blog)
    comment_count=comments.count()

    # Comment form                                         #Actually we need to create form to add comments here blogs is the only field which is accepting slug so we created form directly here..
    if request.method=='POST':
        if not request.user.is_authenticated:
            # Redirect user to login page and come back after login
            return redirect('login')
        comment=Comment()
        comment.user=request.user           #user,blog,comment comes from Comment model.
        comment.blog=single_blog
        comment.comment=request.POST['comment']    #['comment'] comes from name="comment" field from blogs.html comment section textarea name field.  
        comment.save()
        return HttpResponseRedirect(request.path_info)  #HttpResponseRedirect(request.path_info) is used to redirect user to that particular form the form which user commented.

    context={
        'single_blog' : single_blog,
        'random_categories' :random_categories,
        'comments' : comments,
        'comment_count' : comment_count,
    }
    return render(request,'blogs.html',context)


# search bar views

def search(request):
    keyword=request.GET.get('keyword').strip()
    blogs=Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status='Published')

    context={
        'blogs' : blogs,
        'keyword' : keyword,
    }
    return render(request,'search.html',context)



