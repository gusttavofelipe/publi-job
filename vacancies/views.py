from django.http import HttpResponse
from django.shortcuts import render

from vacancies.models import Vacancy

from django.views import View
from django.views.generic.list import ListView


class VacancyHome(ListView):
    model = Vacancy
    template_name = 'vacancies/index.html'
    context_object_name = 'vacancies'


class VacancyDetail(View): pass


class VacancySearch(VacancyHome): pass


class VacancyCategory(VacancyHome): pass

