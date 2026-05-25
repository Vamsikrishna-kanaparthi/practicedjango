from django.db import models

# Create your models here.
class student(models.Model):
    studentid=models.IntegerField()
    studentname=models.CharField(max_length=50)
    studentmarks=models.IntegerField()