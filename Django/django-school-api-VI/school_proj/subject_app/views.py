from django.shortcuts import render, get_object_or_404
from .serializers import Subject, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class All_subjects(APIView):

    def get(self, request):
        subjects = SubjectSerializer(Subject.objects.all(), many=True)
        return Response(subjects.data)
    
class A_subject(APIView):

    def get(self, request, id):
        subject = None
        if type(id) == int:
            subject = get_object_or_404(Subject, id=id)
        else:
            subject = get_object_or_404(Subject, subject_name = id.title())
    
        return Response(SubjectSerializer(subject).data)