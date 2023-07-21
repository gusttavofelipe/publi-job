from categories.models import Category
from occupation.models import Occupation


def all_categories(request):
    return {
        'categories': Category.objects.all(),
    }

def all_occupations(request):
    return {
        'all_occupations': Occupation.objects.all(),
    }