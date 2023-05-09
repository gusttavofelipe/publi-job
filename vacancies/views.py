from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from vacancies.models import Vacancy
from categories.models import Category

from django.views import View
from django.views.generic.list import ListView


class VacancyHome(ListView):
    model = Vacancy
    template_name = 'vacancies/index.html'
    context_object_name = 'vacancies'


class VacancyDetail(View): pass


class VacancySearch(VacancyHome): pass


class VacancyCategory(VacancyHome):
    model = Category
    template_name = 'vacancies/vacancy_category.html'
    context_object_name = 'categories'