from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('user/register/', views.UserRegister.as_view(), name='user_register'),
    path('user/login/', views.UserLogin.as_view(), name='user_login'),
    path('user/logout/', views.UserLogout.as_view(), name='user_logout'),
    path('user/profile/', views.UserProfile.as_view(), name='user_profile'),
    path('user/send_vacancy/', views.SendVacancy.as_view(), name='send_vacancy'),
]