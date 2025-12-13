"""
URL configuration for ilmnote project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static  #mediafile configuration
from django.conf import settings            #mediafile configuration
from blogs import views as Blogsview

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('ilmNote/secure-admin-thahir/', admin.site.urls),  # Rename admin from /admin 


    path('',views.home,name='home'),
    path('category/',include('blogs.urls')),
    path('about/',views.about,name='about'),
    # searchbar
    path('blogs/search/',Blogsview.search,name='search'),
    path('blogs/<slug:slug>/', Blogsview.blogs,name='blogs'),  #for each blog
    # Register
    path('register/',views.register,name='register'),
    # login
    path('login/',views.login,name='login'),
    # logout
    path('logout/',views.logout,name='logout'),
    # dashboard 
    path('dashboard/',include('dashboard.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #mediafile configuration