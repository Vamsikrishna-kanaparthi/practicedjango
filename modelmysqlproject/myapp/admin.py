from django.contrib import admin
from myapp.models import student
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=["id","stuid","stuname","stumarks"]
admin.site.register(student,studentAdmin)