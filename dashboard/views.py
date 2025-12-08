from django.shortcuts import render,redirect,get_object_or_404
from blogs . models import Category,Blog 
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm
from django.contrib import messages
from django.template.defaultfilters import slugify

# Create your views here.

# Dashboard field
@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context={
        'category_count' : category_count,
        'blogs_count' : blogs_count,
    }
    return render(request,'dashboard/dashboard.html',context)
# ---------------------------------------------------
# Dashboard Categories field
def categories(request):
    return render(request,'dashboard/categories.html')

# add categories
def add_categories(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created.")
            return redirect('categories')
    else:
        form=CategoryForm()

    context={
        'form' : form,
    }
    return render(request,'dashboard/add_categories.html',context)

# Edit Categories

def edit_categories(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm(instance=category)

    context={
        'category' : category,
        'form' : form,
    }
    return render(request,'dashboard/edit_categories.html',context)

# Delete Category

def delete_categories(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('categories')

    return render(request, "dashboard/delete_category_confirm.html", {"category": category})
# ----------------------------------------------------------------
# Posts Dashboard 
def posts(request):
    posts=Blog.objects.all()
    context={
        'posts' : posts,
    }
    return render(request,'dashboard/posts.html',context)

# add posts
def add_posts(request):
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)   #request.FILES is used here because form is accepting media like photo here 
        if form.is_valid():
            post=form.save(commit=False)  #temperorly saving form 
            post.author=request.user   #filling author field here in the form 
            post.save()                 #save post so that we can get primary key of the post
            title=form.cleaned_data['title']        #we need to add slug field so here we import title from Blog field
            post.slug=slugify(title)  + '-' + str(post.id)           #this line adds automatic slug field with primary key if two posts have same name (so, test and suppost we have added another post with same name like test for it it will be added primary key test-1 so both are different)
            post.save()                                #save the post after filling slug field
            return redirect('posts')
        else:
            form.errors

    form=BlogForm()
    context={
        'form' : form,
    }
    return render(request,'dashboard/add_posts.html',context)

# Edit Posts

def edit_post(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save()
            # If any body changes title slug need to be updated through uniqueness with the help of pk
            title=form.cleaned_data['title']
            post.slug=slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form=BlogForm(instance=post)
    context={
        'post' : post,
        'form' : form,
    }
    return render(request,'dashboard/edit_post.html',context)

# Delete Post

def delete_post(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request,'dashboard/delete_post_confirm.html', {'post' : post})