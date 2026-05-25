from django.contrib import admin
from myapp.models import student
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ["studentid","studentname","studentmarks"]

admin.site.register(student,studentAdmin)