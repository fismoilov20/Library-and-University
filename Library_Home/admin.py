from django.contrib import admin

from .models import Author, Book, Publisher, Sale, Seller, Student

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Seller)
admin.site.register(Sale)
admin.site.register(Author)
admin.site.register(Student)
