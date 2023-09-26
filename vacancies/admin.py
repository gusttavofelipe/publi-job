from django.contrib import admin

from vacancies.models import Vacancy
from django_summernote.admin import SummernoteModelAdmin


class AdminTools(admin.ModelAdmin):
    list_display = ('name', 'visibility',) 
    list_filter = ('visibility',)
    list_editable = ('visibility',  )
    

admin.site.register(Vacancy, AdminTools)