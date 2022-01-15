from django.contrib import admin
from django.urls import path,include
from . import views
app_name='accounts'
urlpatterns = [
    path("doctors/", views.docter_list, name="doctors"),
    path("login/", views.login_user, name="login"),
    path("signup/", views.signup, name="signup"),

    path("profile/", views.profile, name="profile"),
    path("update_profile/", views.update_profile, name="update_profile"),


    path("<slug:slug>/",views.docter_details, name="doctors_details")
]