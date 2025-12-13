from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [

    # Dashboard
    path('',views.dashboard,name='dashboard'),
    # Category Dashboard Crud
    path('categories/',views.categories,name='categories'),
    path('categories/add/',views.add_categories,name='add_categories'),
    path('categories/edit/<int:pk>/',views.edit_categories,name='edit_categories'),
    path('categories/delete/<int:pk>/',views.delete_categories,name='delete_categories'),
    # Posts Dashboard Crud
    path('posts/',views.posts,name='posts'),
    path('posts/add',views.add_posts,name='add_posts'),
    path('posts/edit/<int:pk>/',views.edit_post,name='edit_post'),
    path('posts/delete/<int:pk>/',views.delete_post,name='delete_post'),
    # Users Dashboard Crud
    path('users/',views.users,name='users'),
    path('users/add/',views.add_user,name='add_user'),
    path('users/edit/<int:pk>/',views.edit_user,name='edit_user'),
    path('users/delete/<int:pk>/',views.delete_user,name='delete_user'),

]