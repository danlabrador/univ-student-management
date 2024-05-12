from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name