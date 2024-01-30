from django.urls import path
from .views import Noun_Project

urlpatterns = [
    path('<str:types>/', Noun_Project.as_view(), name="noun_project"),
]