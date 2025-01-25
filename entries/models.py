from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    # student_id = models.IntegerField() # using built in model's defailt
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dept = models.CharField(max_length=10)
    class_field = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Sport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    selection = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} in {self.selection}"