from django.urls import path
from .views import *

urlpatterns = [
    path('new', PostAssignment.as_view()),
    path('all', GetAssignment.as_view())
]