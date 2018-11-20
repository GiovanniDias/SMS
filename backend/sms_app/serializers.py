from rest_framework import serializers
from .models import Student, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta():
        model = Course
        fields = ('id', 'code', 'name', 'register_date', 'hourly_load')


class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta():
        model = Student
        fields = "__all__"
