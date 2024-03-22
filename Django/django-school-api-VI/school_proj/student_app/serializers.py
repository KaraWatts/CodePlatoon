from rest_framework import serializers
from .models import Student
from subject_app.models import Subject


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "student_email", "locker_number"]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class StudentAllSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Student
        exclude = ['id']