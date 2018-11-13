from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .models import Student, Course
from .serializers import CourseSerializer


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

