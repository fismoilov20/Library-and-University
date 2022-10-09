from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def courses(request):
    if request.method == 'POST':
        if request.POST.get('major') is None:
            result = False
        else:
            result = True
        e = Course.objects.create(
            name = request.POST.get('name'),
            major= result
        )
        l = request.POST.getlist('program')       # ManytoManyField
        for i in l:
            e.program.add(i)
        e.save()
        return redirect('/courses/')

    word = request.GET.get('stext')                                 # form inputs are stored in GET dictionary  # word=" " of input
    if word is None:
        s = Course.objects.all()
    else:
        s = Course.objects.filter(name__contains=word)
    data = {
        'programs': Program.objects.all,
        'courses': s
    }
    return render(request, 'courses.html', data)

def course_edit(request, num):
    if request.method == 'POST':
        if request.POST.get('major') is None:
            result=False
        else:
            result=True
        m = Course.objects.filter(id=num).update(
            name=request.POST.get('name'),
            major=result
        )
        l=request.POST.getlist('program')
        for i in l:
            m.program.add(i)
        m.save()
        
    data = {
        'course':Course.objects.get(id=num),
        'programs':Program.objects.all,
    }
    return render(request, 'course_edit.html', data)

def course_delete(request, num):
    Course.objects.get(id=num).delete()
    return redirect('/courses/')

def programs(request):
    if request.method == 'POST':
        if request.POST.get('active') == 'on':
            result = True
        else:
            result = False
        Program.objects.create(
            name = request.POST.get('name'),
            active = result
        )
        return redirect('/programs/')

    data = {
        'programs': Program.objects.all()
    }
    return render(request, 'programs.html', data)

def program_edit(request, num):
    if request.method == 'POST':
        if request.POST.get('active') == 'on':
            result=True
        else:
            result=False
        Program.objects.filter(id=num).update(
            name=request.POST.get('name'),
            active=result
        )
    data ={
        'program':Program.objects.get(id=num),
    }
    return render(request, 'program_edit.html', data)

def program_delete(request, num):
    Program.objects.get(id=num).delete()
    return redirect('/programs/')

def tutors(request):
    if request.method == 'POST':
        Tutor.objects.create(
            name = request.POST.get('name'),
            degree = request.POST.get('degree'),
            age = request.POST.get('age'),
            gender = request.POST.get('gender'),
            course = Course.objects.get(id=request.POST.get('course'))
        )
        return redirect('/tutors/')

    word = request.GET.get('stext')                                 # form inputs are stored in GET dictionary  # word=" " of input
    if word is None:
        s = Tutor.objects.all()
    else:
        s = Tutor.objects.filter(name__contains=word)
    data = {
        'tutors': s,
        'courses': Course.objects.all
    }
    return render(request, 'tutors.html', data)

def tutor_edit(request, num):
    if request.method == 'POST':
        Tutor.objects.filter(id=num).update(
            name=request.POST.get('name'),
            degree=request.POST.get('degree'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            course=Course.objects.get(id=request.POST.get('course'))
        )
    data = {
        'tutor': Tutor.objects.get(id=num),
        'courses':Course.objects.all,
    }
    return render(request, 'tutor_edit.html', data)

def tutor_delete(request, num):
    Tutor.objects.get(id=num).delete()
    return redirect('/tutors/')

def user_login(request):                    ## View names must NOT be same!
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return redirect('/login/')
        login(request.user)
        return redirect('/')
    return render(request, 'login.html')

def user_logout(request):                    ## View names must NOT be same!
    logout(request.user)
    return redirect('/')

def user_signup(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        return redirect('/login/')
    return render(request, 'signup.html', )