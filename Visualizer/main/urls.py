from django.urls import path
from . import views
  
urlpatterns = [
    path("", views.visualization, name="visualization"),
    path("insights/", views.insights, name="insights"),
]