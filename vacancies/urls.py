from django.urls import path
from . import views


app_name = "vacancies"

urlpatterns = [
    path("", views.VacancyHome.as_view(), name="home"),
    path("vacancy/<int:pk>", views.vacancy_detail_view, name="vacancy_detail"),
    path("search/", views.VacancySearch.as_view(), name="vacancy_search"),
    path("my_vacancies/", views.MyVacancies.as_view(), name="my_vacancies"),
    path(
        "vacancy_category/<str:category>",
        views.VacancyCategory.as_view(),
        name="vacancy_category",
    ),
    path(
        "filter/by-state/<str:state>",
        views.VacancyStateFilter.as_view(),
        name="state_filter",
    ),
    path("send_vacancy/", views.send_vacancy, name="send_vacancy"),
]
