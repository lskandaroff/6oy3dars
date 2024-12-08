from django.shortcuts import render
from .models import Category, Post, Course, Student

def home(request):
    posts = Post.objects.all()
    print(posts)

    return render(request, 'index.html', {'posts': posts})

def student_and_course(request):
    student = Student.objects.all()
    course = Course.objects.all()
    print(course)

    return render(request, 'student_and_course.html', {'student': student, 'course': course})
