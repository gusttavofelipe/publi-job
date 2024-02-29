from django.urls import path
from . import views


app_name = "user"

urlpatterns = [
    path("user/register/", views.UserRegister.as_view(), name="user_register"),
    path("user/login/", views.UserLogin.as_view(), name="user_login"),
    path("user/logout/", views.UserLogout.as_view(), name="user_logout"),
    path("user/view_profile/", views.UserProfile.as_view(), name="user_profile"),
    path("user/edit_user/", views.EditUserInformation.as_view(), name="edit_user"),
    path(
        "profile/<int:id>/update/",
        views.edit_profile_information,
        name="update_profile",
    ),
    path(
        "user/change_password/", views.ChangePassword.as_view(), name="change_password"
    ),
]
