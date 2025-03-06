from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','image','roll','age','religion','gender','city']
    search_fields = ['name','roll']

admin.site.register(Student,StudentAdmin)
admin.site.register(Hobby)
admin.site.register(Result)
admin.site.register(Subject)

