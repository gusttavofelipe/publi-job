from categories.models import Category
from occupation.models import Occupation
from state.models import State


def all_categories(request):
    return {
        'categories': Category.objects.all(),
    }

def all_occupations(request):
    return {
        'all_occupations': Occupation.objects.all(),
    }

def all_states(request):
    return {
        'all_states': State.objects.all()
    }
