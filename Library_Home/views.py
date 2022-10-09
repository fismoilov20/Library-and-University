from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def detail(request, question_id):
    return HTTPResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HTTPResponse(response % question_id)

def vote(request, question_id):
    return HTTPResponse("You're voting on question %s." % question_id)