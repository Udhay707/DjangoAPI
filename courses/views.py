from django.shortcuts import render
from .models import Course
from .serializer import CourseSerializer
from rest_framework import serializers, viewsets

from courses import serializer
# Create your views here.

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


