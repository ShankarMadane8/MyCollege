

from django import forms
from .models import Student,Files


     #student Form

class StudentForm(forms.ModelForm):
  password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
  confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
  prn_no=forms.IntegerField(label="PRN No",widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))

  class Meta:
    model=Student
    fields=('first_name','last_name',"roll_no","prn_no",'email','password','confirm_password')
    
    widgets={
          "first_name":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "last_name":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "roll_no":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "email":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
      }
  def clean(self):
    cleaned_data = super(StudentForm, self).clean()
    password = cleaned_data.get("password")
    confirm_password = cleaned_data.get("confirm_password")

    if password != confirm_password:
      raise forms.ValidationError(
                "password and confirm_password does not match"
            )

   
        # Files Form

class FilesForm(forms.ModelForm):
  upload_file=forms.FileField()
  class Meta:
    model=Files
    fields=("email","upload_file","file_information")
    widgets={                           
          "email":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
          "file_information":forms.TextInput(attrs={'class':'form-control form-control-sm'}),
      }


