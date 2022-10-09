from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Author, Book, Record, Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ('name','id')               # "," must be at the end if tuple items are only one
    list_display = ('id', 'name', 'gender', 'num_of_books')
    list_display_links = ('name', 'gender')
    list_editable = ('num_of_books',)       # "," must be at the end if tuple items are only one
    list_filter = ('gender',)
    list_per_page = 10
    
@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    search_fields = ('name', 'id')
    list_display = ('id', 'name', 'birth_year', 'alive', 'num_of_books')
    list_display_links = ('name',)
    list_editable = ('num_of_books', 'alive')
    list_filter = ('alive',)

@admin.register(Record)
class RecordAdmin(ModelAdmin):
    search_fields = ('student__name', 'book__name')
    list_filter = ('returned',)
    list_display = ('id', 'student', 'book','returned')
    autocomplete_fields = ('student','book')                          # when adding a record among 2000 students

@admin.register(Book)
class BookAdmin(ModelAdmin):
    search_fields = ('name', 'author__name', 'genre')
    list_filter = ('genre',)
    autocomplete_fields = ('author',)                                 # when adding a record among 2000 students



# import sqlite3
# with sqlite3.connect('db.sqlite3') as warehouse:
