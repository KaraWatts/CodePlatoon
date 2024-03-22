from django.db import models
from django.core import validators as v
from student_app.models import Student
from subject_app.models import Subject


# Create your models here.
class Grade(models.Model):
    grade = models.DecimalField(
        default=100.00,
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False,
        validators=[v.MaxValueValidator(100.00), v.MinValueValidator(0.00)],
    )
    a_subject = models.ForeignKey(Subject, related_name="grades", on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, related_name="grades", on_delete=models.SET_NULL, null=True)
