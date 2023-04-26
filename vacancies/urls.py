from django.urls import path
from . import views


urlpatterns = [
    path('', views.VacancieHome.as_view(), name='home'),
    path('vacancie/<int:pk>', views.VacancieDetail.as_view(), name='vacancie_detail'),
    path('search/', views.VacancieSearch.as_view(), name='vacancie_search'),
    path('category/<str:category>', views.VacancieCategory.as_view(), name='vacancie_category'),
]

