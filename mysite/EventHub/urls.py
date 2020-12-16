from django.urls import path
from . import views
app_name = "EventHub"

urlpatterns = [
    
    path("", views.homepage,name="homepage"),


]