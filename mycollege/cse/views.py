from distutils.command.upload import upload
import email
from django.shortcuts import render ,redirect
from .forms import StudentForm,FilesForm
from .models import Student,Files
# Create your views here.

def signup(request):
  if request.session.get("user")!=None:
    return redirect("dashboard")
  msg=''
  if request.method=='POST':
    fm=StudentForm(request.POST)
    if fm.is_valid():
      print("data save  ---------------------------  ")
      fm.save()
      msg="your are successfully registerd !!!"
  else:
    fm=StudentForm()
  return render(request,'cse/signup.html',{"forms":fm,'msg':msg})



def login(request):
  if request.session.get("user")!=None:
    return redirect("dashboard")

  if request.method=="POST":    
    email=request.POST['email']
    password=request.POST['password']
    errors=None     
    try:
      student=Student.objects.get(email=email)
    except:
      errors='Enter valid email and password !!!'
      
    if not errors:
      if password==student.password:
        request.session["user"]=student.first_name
        request.session["email"]=student.email
        return redirect("dashboard")
      else:
        errors='Enter valid  password !!!'
    
    fm=StudentForm()
    return render(request,'cse/login.html',{"forms":fm,"errors":errors})

  else:
  

    fm=StudentForm()
    return render(request,'cse/login.html',{"forms":fm})


def logout(request):
  request.session.flush()
  return redirect('login')


def fileupload(request):
  if request.session.get("user")==None :
    return redirect("login")
  msg=''
  if request.method=='POST':
    print("--------------------",request.FILES,"--------------------")
    fm=FilesForm(data=request.POST,files=request.FILES)
    if fm.is_valid(): 
      if request.session.get("email")!=fm.cleaned_data["email"]:
        msg="enter valid email !!!"
      else:        
        fm.save()
        print("data save  ---------------------------   ")  
        msg="successfully File Upload !!!"

  else:
    fm=FilesForm()
  return render(request,'cse/fileupload.html',{"forms":fm,'msg':msg})



def dashboard(request):
  print("----------",request.session.get("user"))
  if request.session.get("user")==None:  
    return redirect("login")
  del_id=request.GET.get("id")
  if del_id:
    file=Files.objects.filter(id=del_id)
    file.delete()
  search=request.GET.get("search") 
  print(search)
  files=Files.objects.all()  
  user=request.session.get("user")
  if search==None:
    students=Student.objects.all().order_by("roll_no")
  else:
    students=Student.objects.filter(first_name__icontains=search)
  return render(request,'cse/dashboard.html',{"user":user,"files":files,"students":students,"search":search})


def update(request,id):
  msg=""
  if request.method=="POST":
    file=Files.objects.get(id=id)
    fm=FilesForm(request.POST,request.FILES,instance=file)
    if fm.is_valid():
      fm.save()
      msg="update data successfuly !!!"
  else:
    file=Files.objects.get(id=id)
    fm=FilesForm(instance=file)
  return render(request,'cse/fileupload.html',{"forms":fm,"msg":msg})
