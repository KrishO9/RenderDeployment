from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("<h1> Hello There </h1> <p> Just the home page </p>")

def greet_view(request, name):
    """Greets user based on name"""
    greeting_html = f"<h1>Hello, {name}!</h1><p>Nice to meet you.</p>"
    return HttpResponse(greeting_html)

# Create your views here.
