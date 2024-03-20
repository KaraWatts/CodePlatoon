from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null = False, blank = False)
    student_email = models.EmailField(null = False, blank = False)
    personal_email = models.EmailField(null = False, blank = False)
    locker_number = models.IntegerField(default=1, null = False, blank = False)
    locker_combination = models.CharField(max_length=20, null = False, blank = False)
    good_student = models.BooleanField()