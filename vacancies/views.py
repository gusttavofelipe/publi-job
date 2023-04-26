from django.shortcuts import render

from django.views import View
from django.views.generic.list import ListView



class VacancieHome(ListView): pass


class VacancieDetail(View): pass


class VacancieSearch(ListView): pass


class VacancieCategory(ListView): pass

