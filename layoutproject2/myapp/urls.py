from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home),
    path('register/',views.register),
    path('about/',views.about),
    path('contact/',views.contact),
    path('login/',views.login),
]