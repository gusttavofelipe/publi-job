from vacancies.models import Vacancy
from django.views.generic.list import ListView
from django.shortcuts import render


class VacancyHome(ListView):
    model = Vacancy
    template_name = 'vacancies/index.html'
    context_object_name = 'vacancies'


def vacancy_detail_view(request, pk):
    context ={}
    context['vacancy'] = Vacancy.objects.get(id=pk)
    return render(request, "vacancies/detail.html", context)


class VacancySearch(VacancyHome): pass


class VacancyCategory(VacancyHome):
    template_name = 'vacancies/vacancy_category.html'
    
    def get_queryset(self):
        category = self.kwargs.get('category', None)

        qs = Vacancy.objects.filter(category__name=category)        
        return qs


class VacancyForm(VacancyHome):
    template_name = 'vacancies/form.html'


class VacancyLogin(VacancyHome):
    template_name = 'vacancies/register.html'

