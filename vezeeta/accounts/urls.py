from django.contrib import admin
from django.urls import path,include
from . import views
app_name='accounts'
urlpatterns = [
    path("", views.docter_list, name="_doctors"),
    path("doctors/", views.docter_list, name="doctors"),
    path("login/", views.login_user, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("make_order/<slug:slug>/",views.make_order, name="make_order"),
    path("order_complete/",views.order_complete, name="order_complete"),
    # path("contact_us/", views.contact_us, name="contact_us"),
    path("<slug:slug>/",views.docter_details, name="doctors_details"),

]