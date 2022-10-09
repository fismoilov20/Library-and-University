from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Course, Program, Tutor

# Register your models here.

@admin.register(Course)
class CourseAdmin(ModelAdmin):
    search_fields = ('name', 'program__name')
    list_filter = ('major',)
    list_display = ('id','name','major')
    list_display_links = ('name',)
    autocomplete_fields = ('program',)


@admin.register(Program)
class ProgramAdmin(ModelAdmin):
    search_fields = ('name',)
    list_filter = ('active',)
    list_display = ('id','name','active')

@admin.register(Tutor)
class TutorAdmin(ModelAdmin):
    search_fields = ('name','degree','course__name')
    list_filter = ('gender','degree')
    list_display = ('name', 'course', 'degree','gender','age')