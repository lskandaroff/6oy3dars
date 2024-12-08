from django.urls import path
from .views import home, student_and_course

urlpatterns = [
    path('', home),
    path('student_and_course', student_and_course)
    ]