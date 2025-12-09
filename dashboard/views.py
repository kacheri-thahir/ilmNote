from django.shortcuts import render,redirect,get_object_or_404
from blogs . models import Category,Blog 
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm,AddUserForm,EditUserForm
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.

# creating one function staff_only decorator to access dashboard only for staff members not for normal users put @staff_only to all views which only staff access. If any users cracks urls for dashboard and cleverly goes to access it django throws 404 error
def staff_only(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_staff:
            raise Http404
        return view_func(request, *args, **kwargs)
    return wrapper



# Dashboard field
@login_required(login_url='login')
@staff_only
def dashboard(request):
    if not request.user.is_staff:
        raise Http404

    category_count=Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context={
        'category_count' : category_count,
        'blogs_count' : blogs_count,
    }
    return render(request,'dashboard/dashboard.html',context)
# ---------------------------------------------------
# Dashboard Categories field
@staff_only
def categories(request):
    return render(request,'dashboard/categories.html')

# add categories
@staff_only
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
@staff_only
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
@staff_only
def delete_categories(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('categories')

    return render(request, "dashboard/delete_category_confirm.html", {"category": category})
# ----------------------------------------------------------------
# Posts Dashboard 
@staff_only
def posts(request):
    posts=Blog.objects.all()
    context={
        'posts' : posts,
    }
    return render(request,'dashboard/posts.html',context)

# add posts
@staff_only
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
            messages.success(request, "Post created.")
            return redirect('posts')
        else:
            form.errors

    form=BlogForm()
    context={
        'form' : form,
    }
    return render(request,'dashboard/add_posts.html',context)

# Edit Posts
@staff_only
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
@staff_only
def delete_post(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request,'dashboard/delete_post_confirm.html', {'post' : post})

# -----------------------------------------------------

# Dashboard Users Field
@staff_only
def users(request):
    users=User.objects.all()
    context={
        'users' : users
    }
    return render(request,'dashboard/users.html',context)

# Add Users
@staff_only
def add_user(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form=AddUserForm()
    context={
        'form' : form,
    }
    return render(request,'dashboard/add_user.html',context)

# Edit User
@staff_only
def edit_user(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method=='POST':
        form=EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form=EditUserForm(instance=user)
    context={
        'form' : form
    }
    return render(request,'dashboard/edit_user.html',context)

# Delete User
@staff_only
def delete_user(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    return render(request,'dashboard/delete_user_confirm.html',{'user':user})