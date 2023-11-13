from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(AbstractUser):
    birthdate = models.DateField(null = True)
    phone = models.CharField(max_length=12, null = True)
    courses = models.ManyToManyField(Course, related_name='students', null = True)