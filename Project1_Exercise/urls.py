"""Project1_Exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Library.views import *
from University.views import *

# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('view/', view),
    
    path('page1/', view1),
    path('seniors/', view3),

    path('students/', students),
    path('std/<int:num>/', std_details),       #.../std/5
    path('std_edit/<int:num>/', std_edit),       #.../std_edit/5
    path('std_delete/<int:num>/', std_delete),           # delete
    path('std_confirm/<int:num>/', std_confirm),

    path('books/', books),       
    path('books/<int:num>/', book_details),
    path('book_delete/<int:num>/', book_delete),          # delete

    path('authors/', authors),       
    path('authors/<int:num>/', author_details),
    path('author_edit/<int:num>/', author_edit),
    path('author_delete/<int:num>/', author_delete),

    path('records/', records),       
    path('records/<int:num>/', record_details),
    path('record_edit/<int:num>/', record_edit),
    path('record_delete/<int:num>/', record_delete),

    path('courses/', courses),
    path('course_edit/<int:num>/', course_edit),
    path('course_delete/<int:num>/', course_delete),

    path('programs/', programs),
    path('program_edit/<int:num>/', program_edit),
    path('program_delete/<int:num>/', program_delete),

    path('tutors/', tutors),
    path('tutor_edit/<int:num>/', tutor_edit),
    path('tutor_delete/<int:num>/', tutor_delete),

    path('login/', loginView),
    path('logout/', logoutView),
    path('', index),
    path('signup/', signup),
    
    path('logout/', user_logout),
    path('login/', user_login),
    path('signup/', user_signup),

    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
