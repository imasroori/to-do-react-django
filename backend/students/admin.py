from django.contrib import admin

# Register your models here.
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'document', 'phone', 'registrationDate']


admin.site.register(Student, StudentAdmin)
