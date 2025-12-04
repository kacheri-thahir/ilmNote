from django.contrib import admin
from . models import Category,Blog,About,Socialmedia_links
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category','status','is_featured')
    search_fields=('id','title','category__category_name','status')
    list_editable=('is_featured',)    #to make is_featured editable on SQLite DB



# This will only give permission to add single About description not more than one will add in about section

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=About.objects.all().count()
        if count==0:
            return True
        return False
        

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Socialmedia_links)

