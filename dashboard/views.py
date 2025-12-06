from django.shortcuts import render,redirect,get_object_or_404
from blogs . models import Category,Blog 
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
from django.contrib import messages

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
