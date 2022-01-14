from django.contrib import admin
from django.urls import path,include
from . import views
app_name='accounts'
urlpatterns = [
    path("doctors/", views.docter_list, name="doctors"),
     path("login/", views.login_user, name="login"),
    path("profile/", views.profile, name="profile"),


    path("<slug:slug>/",views.docter_details, name="doctors_details")
]