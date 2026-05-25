from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1 style='text-align:center;color:blue'>Home Page</h1>")

def login(request):
    return HttpResponse("<h1 style='text-align:center;color:blue'>Login Page</h1>")

def register(request):
    return HttpResponse("<h1 style='text-align:center;color:blue'>Register</h1>")
