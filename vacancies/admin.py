from django.contrib import admin

from vacancies.models import Vacancie
from django_summernote.admin import SummernoteModelAdmin


# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('about_company',)

admin.site.register(Vacancie)