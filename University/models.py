from unicodedata import name
from django.db import models

# Create your models here.

class Program(models.Model):
    name = models.CharField(max_length=35)
    active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=35)
    program = models.ManyToManyField(Program)                                           # FK
    major = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name

class Tutor(models.Model):
    name = models.CharField(max_length=35)
    degree = models.CharField(max_length=35, choices=(('B','Bachelor'),('M','Master'),('D','Doctor')))
    age = models.PositiveSmallIntegerField(null=True,blank=True)
    gender = models.CharField(max_length=25, choices=(("MALE","Male"), ("FEMALE","Female")))
    course = models.ForeignKey(Course,on_delete=models.CASCADE)                                             # FK
    def __str__(self) -> str:
        return self.name
