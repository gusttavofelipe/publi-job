from categories.models import Category
from occupation.models import Occupation
from state.models import State
from user.models import Profile


def all_categories(request):
    return {
        "categories": Category.objects.all(),
    }


def all_occupations(request):
    return {
        "all_occupations": Occupation.objects.all(),
    }


def all_states(request):
    return {"all_states": State.objects.all()}


def all_profiles(request):
    return {"all_profiles": Profile.objects.all()}
