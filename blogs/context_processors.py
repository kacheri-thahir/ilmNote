from . models import Category

# This Context Processors used to get all the categories on every page on app

def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)