import email
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *

from .forms import *
from .models import *

# Create your views here.

def view(request):
    return HttpResponse("Hello World!")         # returns HttpResponse

def index(request):
    auth = request.user.is_authenticated

    data = {
        'auth': auth
    }
    return render(request, 'index.html', data)        # returns html

def view1(request):
    data = {
        'name':'Ransomware',
        'names':['Bob','Kelvin','George','Ford']
        }
    return render(request, 'index1.html', data)

def view3(request):
    data = {
        'std_list': Student.objects.filter(senior=True)
    }
    return render(request, 'folder/senior_stds.html', data)

def students(request):
    if request.user.is_authenticated:
        if request.method == 'POST':      
            f = StudentForm(request.POST)
            if f.is_valid():
                Student.objects.create(
                    name = f.cleaned_data.get('name'),
                    gender = f.cleaned_data.get('gender'),
                    num_of_books = f.cleaned_data.get('num_of_books'),
                    senior = f.cleaned_data.get('senior')
                ) 
            return redirect('/students/')

        word = request.GET.get('stext')                         # form inputs are stored in GET dictionary  # word=" " of input
        if word is None:
            s = Student.objects.all()
        else:
            s = Student.objects.filter(name__contains=word)
        
        data = {
            'students_list': s,
            'form': StudentForm,
        }
        return render(request, 'students.html', data)
    else:
        return redirect('/login/')

def std_details(request, num):
    data = {
        'std': Student.objects.get(id=num)
    }
    return render(request, 'std_details.html', data)

def std_edit(request, num):
    if request.method == 'POST':
        if request.POST.get('senior') is None:
            result = False
        else:
            result = True
        Student.objects.filter(id=num).update(
            name = request.POST.get('name'),
            senior=result,
            num_of_books=request.POST.get('num_of_books')
        )
        return redirect('/students/')

    data = {
        'student': Student.objects.get(id=num),
    }
    return render(request, 'std_edit.html', data)

def std_delete(request, num):
    Student.objects.get(id=num).delete()
    return redirect('/students/')

def std_confirm(request, num):
    data = {
        'student': Student.objects.get(id=num)
    }
    return render(request, 'std_confirm.html', data)

def books(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f = BookForm(request.POST)
            if f.is_valid():
                f.save()
            return redirect('/books/')

        data = {
            'books'  :  Book.objects.all(),
            'form'   :  BookForm
        }
        return render(request, 'books.html', data)
    else:
        return redirect('/login/')

def book_details(request, num):
    data = {
        'book': Book.objects.get(id=num)
    }
    return render(request, 'book_details.html', data)

def book_delete(request, num):
    Book.objects.get(id=num).delete()
    return redirect('/books/')

def authors(request):
    if request.user.is_authenticated:
        if request.method == 'POST':      
            f = AuthorForm(request.POST)
            if f.is_valid():
                f.save()
            return redirect('/authors/')

        word = request.GET.get('stext')                         # form inputs are stored in GET dictionary  # word=" " of input
        if word is None:
            s = Author.objects.all()
        else:
            s = Author.objects.filter(name__contains=word)

        data = {
            'authors': s,
            'form': AuthorForm
        }
        return render(request, 'authors.html', data)
    else:
        return redirect('/login/')

def author_details(request, num):
    data = {
        'author': Author.objects.get(id=num)
    }
    return render(request, 'author_details.html', data)

def author_edit(request, num):
    if request.method == 'POST':
        if request.POST.get('alive') is None:
            result = False
        else:
            result = True
        Author.objects.filter(id=num).update(
            name = request.POST.get('name'),
            birth_year=request.POST.get('birth_year'),
            alive=result,
            num_of_books=request.POST.get('num_of_books')
        )
        return redirect('/authors/')

    data = {
        'author': Author.objects.get(id=num),
    }
    return render(request, 'author_edit.html', data)

def author_delete(request, num):
    Author.objects.get(id=num).delete()
    return redirect('/authors/')

def records(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f = RecordForm(request.POST)
            if f.is_valid():
                f.save()
            return redirect('/records/')

        word = request.GET.get('stext')                    # form inputs are stored in GET dictionary  # word=" " of input
        if word is None:
            s = Record.objects.all()
        else:
            s = Record.objects.filter(student__name__contains=word)

        data = {
            'records': s,
            'form': RecordForm
        }
        return render(request, 'records.html', data)
    else:
        return redirect('/login/')

def record_details(request, num):
    data = {
        'record': Record.objects.get(id=num)
    }
    return render(request, 'record_details.html', data)

def record_edit(request, num):
    if request.method == 'POST':
        if request.POST.get('returned') is None:
            result = False
        else:
            result = True
        Record.objects.filter(id=num).update(
            returned_date=request.POST.get('returned_date'),
            returned=result,
        )
        return redirect('/records/')

    data = {
        'record': Record.objects.get(id=num),
        'students':Student.objects.all,
        'books': Book.objects.all,
    }
    return render(request, 'record_edit.html', data)

def record_delete(request, num):
    Record.objects.get(id=num).delete()
    return redirect('/records/')

def loginView(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return redirect('/login/')
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        return redirect('/login/')
    return render(request, 'signup.html')