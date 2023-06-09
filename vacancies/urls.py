from django.urls import path
from . import views


app_name ='vacancies'

urlpatterns = [
    path('', views.VacancyHome.as_view(), name='home'),
    path('vacancy/<int:pk>', views.vacancy_detail_view, name='vacancy_detail'),
    path('search/', views.VacancySearch.as_view(), name='vacancy_search'),
    path('vacancy_category/<str:category>', views.VacancyCategory.as_view(), name='vacancy_category'),
    path('send_vacancy/', views.send_vacancy, name='send_vacancy'),
]

