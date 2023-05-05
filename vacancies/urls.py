from django.urls import path
from . import views


urlpatterns = [
    path('', views.VacancyHome.as_view(), name='home'),
    path('vacancy/<int:pk>', views.VacancyDetail.as_view(), name='vacancy_detail'),
    path('search/', views.VacancySearch.as_view(), name='vacancy_search'),
    path('category/<str:category>', views.VacancyCategory.as_view(), name='vacancy_category'),
]

