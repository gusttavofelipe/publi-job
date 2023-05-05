from django.contrib import admin

from vacancies.models import Vacancy
from django_summernote.admin import SummernoteModelAdmin


# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('about_company',)

admin.site.register(Vacancy)