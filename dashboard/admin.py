# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# # Register your models here.

# class CustomUserAdmin(DefaultUserAdmin):
#     def get_readonly_fields(self, request, obj=None):
#         fields = super().get_readonly_fields(request, obj)
#         if not request.user.is_superuser:
#             fields += ('is_superuser', 'groups', 'user_permissions')
#         return fields

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if not request.user.is_superuser:
#             return qs.filter(is_superuser=False)
#         return qs

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)



from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .admin_site import secure_admin_site
from blogs.models import Blog, Category,About,Socialmedia_links,Comment # example: your other models

# Register the User model with custom restrictions
class CustomUserAdmin(DefaultUserAdmin):
    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            fields += ('is_superuser', 'groups', 'user_permissions')
        return fields

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(is_superuser=False)
        return qs

secure_admin_site.register(User, CustomUserAdmin)
# what we need to display in admin page for superuser need to register here....
secure_admin_site.register(Group)  # if you want groups visible
secure_admin_site.register(Blog)   # your app models
secure_admin_site.register(Category)
secure_admin_site.register(About)
secure_admin_site.register(Socialmedia_links)
secure_admin_site.register(Comment)
