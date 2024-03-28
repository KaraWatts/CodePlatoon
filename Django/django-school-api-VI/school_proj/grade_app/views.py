from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from .models import Grade, Subject, Student
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
# Create your views here.

    

class A_grade(APIView):

    def delete(self, request, student_id):
        subject = request.data.get("subject_id")
        grade = get_object_or_404(Grade, student__id = student_id, a_subject__id = subject)
        grade.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def put(self, request, student_id):
        subject = request.data.get("subject_id")
        grade = get_object_or_404(Grade, student__id = student_id, a_subject__id = subject)
        grade.grade = request.data.get("grade")
        grade.save()
        return Response(status=HTTP_200_OK)
    
    def post(self, request, student_id):
        subject = Subject.objects.get(id=request.data.get('subject_id'))
        student = Student.objects.get(id=student_id)
        grade = request.data.get("grade")

        new_grade = Grade(grade=grade, a_subject=subject, student=student)
        new_grade.save()
        return Response(status=HTTP_201_CREATED)

