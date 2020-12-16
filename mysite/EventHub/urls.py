from django.urls import path
from . import views

app_name = "EventHub"

urlpatterns = [

    path("", views.home,name="home"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("eventpage/", views.eventpage, name="eventpage"),


]