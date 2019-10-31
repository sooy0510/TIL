from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
  students = Student.objects.all()[::-1] #python
  context = {'students':students}
  return render(request,'students/index.html', context)


def new(request):
  return render(request,'students/new.html')


def create(request):
  name = request.POST.get('name')
  birthday = request.POST.get('birthday')

  student = Student(name=name, birthday=birthday)
  # save까지하고 나면 pk값 부여됨
  student.save()
  return redirect('students:index')