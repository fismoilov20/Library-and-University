from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=25)
    birth_year = models.PositiveIntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)                         # FK
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)          # FK
    date = models.DateField(auto_now_add=True)        
    def __str__(self) -> str:
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=25)
    phonenum = models.CharField(max_length=13)
    def __str__(self) -> str:
        return self.name

class Sale(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)                   # FK
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)               # FK
    date = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.date

class Student(models.Model):
    name = models.CharField(max_length=25)
    senior = models.BooleanField(null=True)
    gender = models.CharField(max_length=25, choices=(("MALE","Male"), ("FEMALE","Female")))
    num_of_books = models.PositiveSmallIntegerField(default=0)
    def __str__(self) -> str:
        return self.name
