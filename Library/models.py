from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    senior = models.BooleanField(null=True)
    gender = models.CharField(max_length=25, choices=(("MALE","Male"), ("FEMALE","Female")))
    num_of_books = models.PositiveSmallIntegerField(default=0)
    def __str__(self) -> str:
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=25)
    birth_year = models.PositiveIntegerField(null=True,blank=True)
    alive = models.BooleanField()
    num_of_books = models.PositiveSmallIntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=25,null=True,blank=True)
    author = models.ManyToManyField(Author)                                         # MtO
    pages = models.PositiveIntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name

class Record(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)                   # FK
    book = models.ForeignKey(Book,on_delete=models.CASCADE)                         # FK
    took_date = models.DateField()
    returned_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.student.name}, {self.book.name}"

