from django.test import TestCase
from .models import Student 
from django.core.exceptions import ValidationError
from django.db import IntegrityError


# Create your tests here.
class Test_student(TestCase):
    def test_001_student_with_improper_good_student_field(self):
        try:
            new_student = Student.objects.create(
                name="John W. Watson",
                student_email="thisIsAnEmail@school.com",
                personal_email="thisIsAnEmail@gmail.com",
                locker_number=13,
                locker_combination = "12-33-44",
                good_student = None
            )

            new_student.full_clean()
            self.fail()
        except IntegrityError as e:
            # print(e)
            self.assertIn('null value in column "good_student" of relation "student_app_student" violates not-null constraint', str(e))

    def test_002_student_with_improper_email_fields(self):
        try:
            new_student = Student.objects.create(
                name="John W. Watson",
                student_email="thisIsNotAnEmail",
                personal_email=False,
                locker_number=13,
                locker_combination = "23-33-44",
                good_student = True
            )
            new_student.full_clean()
            self.fail()
        except ValidationError as e:
            # print(e.message_dict)
            self.assert_('student_email' in e.message_dict and 'personal_email' in e.message_dict)

    def test_003_student_with_improper_locker_number_fields(self):
        try:
            new_student = Student.objects.create(
                name="John W. Watson",
                student_email="thisIsAnEmail@school.com",
                personal_email="thisIsAnEmail@gmail.com",
                locker_number="None",
                locker_combination = "23-33-44",
                good_student = True
            )
            new_student.full_clean()
            self.fail()
        except Exception as e:
            # print(e)
            self.assert_("Field 'locker_number' expected a number but got 'None'" in str(e))

    def test_004_student_with_improper_locker_combination_fields(self):
        try:
            new_student = Student.objects.create(
                name="John W. Watson",
                student_email="thisIsAnEmail@school.com",
                personal_email="thisIsAnEmail@gmail.com",
                locker_number=13,
                locker_combination = None,
                good_student = True
            )
            new_student.full_clean()
            self.fail()
        except IntegrityError as e:
            # print(e)
            self.assert_("null value in column \"locker_combination\" " in str(e))

    def test_005_student_with_improper_name_field(self):
        try:
            new_student = Student.objects.create(
                name=None,
                student_email="thisIsAnEmail@school.com",
                personal_email="thisIsAnEmail@gmail.com",
                locker_number=13,
                locker_combination = "12-12-12",
                good_student = True
            )
            new_student.full_clean()
            self.fail()
        except Exception as e:
            # print(e)
            self.assert_("null value in column \"name\" " in str(e))

    
    def test_006_student_with_proper_fields(self):
        new_student = Student.objects.create(
            name = "John W. Wally",
            student_email = "john@school.com",
            personal_email = "john@gmail.com",
            locker_number = 13,
            locker_combination = "12-12-12",
            good_student = True
        )
        new_student.full_clean()
        self.assertIsNotNone(new_student)
