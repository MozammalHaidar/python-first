from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['prime_id','name','email','image','roll','age','religion','gender','city']
    search_fields = ['name','roll']

admin.site.register(Student,StudentAdmin)

