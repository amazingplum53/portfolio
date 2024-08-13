
from models import Category

def category_context_processor(request):
    return {
        'Categories': Category.objects.all(),
    }
