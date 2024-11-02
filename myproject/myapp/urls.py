
from django.urls import path
from . import views


urlpatterns = [
    path("", views.indexView.as_view(), name="index"),

    # login & register
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),

]