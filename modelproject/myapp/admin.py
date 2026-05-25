from django.contrib import admin
from myapp.models import employee
# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display=["id","eid","ename","esal"]

admin.site.register(employee,employeeAdmin)
    
        
    