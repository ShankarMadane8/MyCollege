from enum import unique
from django.db import models
from django.forms import FileField


# Create your models here.

class Student(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  roll_no=models.IntegerField(unique=True)
  prn_no=models.IntegerField(unique=True)
  email=models.EmailField(unique=True)
  password=models.CharField(max_length=50)
  confirm_password=models.CharField(max_length=50)

  def __str__(self):
    return self.email
  
class Files(models.Model):
  email=models.EmailField()
  upload_file=models.FileField(upload_to='files')
  file_information=models.TextField()

