from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from .models import Grade
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class A_grade(APIView):
    def put(self, request, student_id, subject_id):
        grade = get_object_or_404(Grade, student__id = student_id, a_subject__id = subject_id)
        grade.grade = request.data.get("grade")
        grade.save()
        return Response(status=HTTP_200_OK)

