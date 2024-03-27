from django.urls import path
from .views import A_grade

urlpatterns = [
    path('<int:student_id>/<int:subject_id>/', A_grade.as_view(), name='a_grade')
]