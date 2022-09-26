from django.contrib import admin
from .models import Student,Files
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display=('first_name','last_name',"roll_no","prn_no",'email','password','confirm_password')

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
  list_display=("email","upload_file","file_information")