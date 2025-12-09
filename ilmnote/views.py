from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Category,Blog,About,Socialmedia_links
from . forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login as auth_login

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

# Register

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form=RegisterForm()

    context={
        'form' : form,
    }
    return render(request,'register.html',context)

# login

# def login(request):
#     if request.method=='POST':
#         form=AuthenticationForm(request,request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']                          #This is a custom way to create login page which takes manually checks the username , password valid or not this is not a professional way to write login code it is used when you need custom validation and ui then it will be useful
#             password=form.cleaned_data['password']

#             user=auth.authenticate(username=username,password=password)
#             if user is not None:
#                 auth.login(request,user)
#                 return redirect('home')
#             else:
#                 # form will automatically contain non_field_errors like:
#                 # "Please enter a correct username and password."
#                 return render(request, "login.html", {"form": form})
                
#     form=AuthenticationForm()
#     context={
#         'form' : form,
#     }
#     return render(request,'login.html',context)


# LOGIN 

# This is the professional way to validate and write login code

# The password check happens inside AuthenticationForm.is_valid(), which runs:
# validate username exists
# validate password
# check if user is active
# attach the correct non_field_errors
# So you do not need authenticate() again.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)     #auth_login(request, user) only logs in the user who is already authenticated.
            return redirect('home')

        # If invalid, errors will be inside form.non_field_errors
        return render(request, 'login.html', {'form': form})

    # GET request
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# LOGOUT

def logout(request):
    auth.logout(request)
    return redirect('login')