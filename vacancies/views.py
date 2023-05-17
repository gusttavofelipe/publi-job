from vacancies.models import Vacancy

from django.views import View
from django.views.generic.list import ListView


class VacancyHome(ListView):
    model = Vacancy
    template_name = 'vacancies/index.html'
    context_object_name = 'vacancies'


class VacancyDetail(View): pass


class VacancySearch(VacancyHome): pass


class VacancyCategory(VacancyHome):
    template_name = 'vacancies/vacancy_category.html'
    
    def get_queryset(self):
        category = self.kwargs.get('category', None)

        qs = Vacancy.objects.filter(category__name=category)        
        return qs


class VacancyForm(VacancyHome):
    template_name = 'vacancies/form.html'
