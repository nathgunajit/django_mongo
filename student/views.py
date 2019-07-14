from django.shortcuts import render

# Create your views here.
from .models import Student

def home(request):
    student= Student.objects.all()
    template="student/home.html"
    context={
        'student':student,
    }
   # print(student)
    return render(request,template,context)
