from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def hello_view(request):
    return HttpResponse("Hi, it is my project")
def current_date_view(request):
    return HttpResponse(f"{datetime.now()}")
def goodbye_view(request):
    return HttpResponse("Bye Bye")
