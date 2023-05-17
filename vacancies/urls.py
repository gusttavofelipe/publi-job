from django.urls import path
from . import views


urlpatterns = [
    path('', views.VacancyHome.as_view(), name='home'),
    path('vacancy/<int:pk>', views.VacancyDetail.as_view(), name='vacancy_detail'),
    path('search/', views.VacancySearch.as_view(), name='vacancy_search'),
    path('vacancy_category/<str:category>', views.VacancyCategory.as_view(), name='vacancy_category'),
    path('vacancy_form/', views.VacancyForm.as_view(), name='vacancy_form'),
    path('vacancy_login/', views.VacancyLogin.as_view(), name='vacancy_login'),
]

