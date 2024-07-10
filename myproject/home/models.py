from django.db import models

# Create your models here.

class Student(models.Model):
    #id      =   models.AutoField()             # It will auto created by Django
    name    =   models.CharField(max_length=100)
    age     =   models.IntegerField()
    email   =   models.EmailField(null=True, blank=True)
