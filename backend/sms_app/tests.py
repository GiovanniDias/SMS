from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .models import Student, Course
from .serializers import CourseSerializer, StudentSerializer


class CourseApiTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.course1 = Course.objects.create(
            code='C001',
            name='Administração',
            hourly_load=1800
        )

        self.valid_payload = {
            'code': 'C002',
            'name': 'Direito',
            'hourly_load': 1980
        }

    def test_create(self):
        response = self.client.post('/api/courses/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all(self):
        response = self.client.get('/api/courses/')
        all_courses = CourseSerializer(Course.objects.all(), many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, all_courses)

    def test_get_one(self):
        route = '/api/courses/' + str(self.course1.id) + '/'
        response = self.client.get(route)
        course = CourseSerializer(Course.objects.get(id=self.course1.id)).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, course)

    def test_update(self):
        self.valid_payload['hourly_load'] = 1920
        route = '/api/courses/' + str(self.course1.id) + '/'

        response = self.client.put(
            route, self.valid_payload, content_type='application/json')

        self.assertEqual(response.data.get('hourly_load'),
                         self.valid_payload.get('hourly_load'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        route = '/api/courses/' + str(self.course1.id) + '/'
        response = self.client.delete(route)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class StudentApiTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.course2 = Course.objects.create(
            code='C002',
            name='Direito',
            hourly_load=1980
        )

        self.student1 = Student.objects.create(
            code='A001',
            name='Advogado1',
            cpf='12345678910',
            email='adm@email.com',
            cep='65000000',
            address='Rua A',
            number='10',
            course=self.course2
        )

        self.valid_payload = {
            'code': 'A002',
            'name': 'Promotor2',
            'cpf': '10987654321',
            'phone': '098987654321',
            'email': '',
            'cep': '65310000',
            'address': 'Rua 15, Quadra B',
            'number': 'S/N',
            'complement': '',
            'course': int(self.course2.id)
        }

    def test_create(self):
        response = self.client.post('/api/students/', self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all(self):
        response = self.client.get('/api/students/')
        all_students = StudentSerializer(Student.objects.all(), many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, all_students)

    def test_get_one(self):
        route = '/api/students/' + str(self.student1.id) + '/'
        response = self.client.get(route)
        student = StudentSerializer(
            Student.objects.get(id=self.student1.id)).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, student)

    def test_update(self):
        self.valid_payload['email'] = 'adm2@email.com'
        route = '/api/students/' + str(self.student1.id) + '/'

        response = self.client.put(
            route, self.valid_payload, content_type='application/json')

        self.assertEqual(response.data.get('email'),
                         self.valid_payload.get('email'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        route = '/api/students/' + str(self.student1.id) + '/'
        response = self.client.delete(route)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
