from django.http import HttpResponse
from django.shortcuts import render

from vacancies.models import Vacancie

from django.views import View
from django.views.generic.list import ListView


class VacancieHome(ListView):
    model = Vacancie
    template_name = 'vacancies/index.html'
    context_object_name = 'vacancies'


class VacancieDetail(View): pass


class VacancieSearch(VacancieHome): pass


class VacancieCategory(VacancieHome): pass

