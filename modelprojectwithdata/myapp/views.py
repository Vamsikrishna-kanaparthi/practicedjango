from django.shortcuts import render
from myapp.models import student
from django.http import HttpResponse
# Create your views here.
def home(request):
    students=student.objects.all()
    for stu in students:
        print(f'{stu.studentid}\t{stu.studentname}\t{stu.studentmarks}')
    return HttpResponse("<h1 style ='text-align:center' >home </h1>")

