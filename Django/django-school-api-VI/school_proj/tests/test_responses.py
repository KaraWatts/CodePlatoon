from django.test import TestCase, Client
from django.urls import reverse, resolve
from tests.answers import all_students, all_subjects, a_student, a_subject
import json


class Test_endpoints(TestCase):
    fixtures = [
        "tests/fixtures/subjects.json",
        "tests/fixtures/students.json",
        "tests/fixtures/grades.json",
    ]

    def setUp(self):
        client = Client()

    # PART VI

    def test_01_all_classes(self):
        response = self.client.get(reverse("all_subjects"))
        with self.subTest():
            self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content, all_subjects)

    def test_02_url_pattern_subjects(self):
        url_route = resolve(reverse("all_subjects"))
        self.assertEqual(url_route.route, 'api/v1/subjects/')

    def test_03_all_students(self):
        response = self.client.get(reverse("all_students"))
        with self.subTest():
            self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        # print(all_students)
        self.assertEqual(content, all_students)

    def test_04_url_pattern_students(self):
        url_route = resolve(reverse("all_students"))
        self.assertEqual(url_route.route, 'api/v1/students/')

    # PART VII

    def test_05_get_a_subject(self):
        response = self.client.get(reverse('a_subject', args=['python']))
        with self.subTest():
            self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content, a_subject)

    def test_06_get_a_subject_route(self):
        url_pattern = resolve(reverse('a_subject', args=['python']))
        self.assertEqual(url_pattern.route, 'api/v1/subjects/<int_or_str:id>/')

    def test_07_get_subject_dne(self):
        response = self.client.get(reverse('a_subject', args=['psychology']))
        self.assertEqual(response.status_code, 404)

    def test_08_get_a_student(self):
        response = self.client.get(reverse('a_student', args=[3]))
        with self.subTest():
            self.assertTrue(response.status_code == 200)
        content = json.loads(response.content)
        self.assertEqual(content, a_student)

    def test_09_get_a_student_route(self):
        url_pattern = resolve(reverse('a_student', args=[3]))
        self.assertEqual(url_pattern.route, 'api/v1/students/<int:id>/')

    def test_10_get_student_dne(self):
        response = self.client.get(reverse('a_student', args=[375]))
        self.assertEqual(response.status_code, 404)