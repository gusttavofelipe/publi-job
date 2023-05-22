from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('user_register/', views.UserRegister.as_view(), name='user_register'),
    path('user_login/', views.UserLogin.as_view(), name='user_login'),
    path('user_login/', views.UserLogout.as_view(), name='user_logout'),
]