from django.contrib import admin

from vacancies.models import Vacancy


# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('about_company',)

admin.site.register(Vacancy)
