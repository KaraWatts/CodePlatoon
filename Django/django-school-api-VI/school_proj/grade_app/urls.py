
from django.urls import path
from .views import A_grade

urlpatterns = [
    path('grades/', A_grade.as_view(), name='a_grade'),
]

