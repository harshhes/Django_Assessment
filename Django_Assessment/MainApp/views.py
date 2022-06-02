from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class PostAssignment(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class GetAssignment(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

