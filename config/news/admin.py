from django.contrib import admin

from .models import Category, Post, Course, Student


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Course)
admin.site.register(Student)

# Register your models here.
