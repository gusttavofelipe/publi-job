from django.http import HttpResponse
from django.shortcuts import render

from vacancies.models import Vacancie

from django.views import View
from django.views.generic.list import ListView



class VacancieHome(ListView):
    model = Vacancie
    template_name = 'vacancies/index.html'

    def get_queryset(self):
        HttpResponse('Youre looking at question')


class VacancieDetail(View): pass


class VacancieSearch(ListView): pass


class VacancieCategory(ListView): pass

