from categories.models import Category


def all_categories(request):
    return {
        'categories': Category.objects.all(),
    }