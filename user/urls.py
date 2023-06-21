from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView


app_name = 'user'

urlpatterns = [
    path('user/register/', views.UserRegister.as_view(), name='user_register'),
    path('user/login/', views.UserLogin.as_view(), name='user_login'),
    path('user/logout/', views.UserLogout.as_view(), name='user_logout'),
    path('user/view_profile/', views.UserProfile.as_view(), name='user_profile'),
    path('user/change_data/', views.EditProfile.as_view(), name='edit_profile'),
    path('user/change_password/', views.ChangePassword.as_view(), name='change_password'),
]