from django.shortcuts import render
from .models import students
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def Learners(request):
   context ={
      'learners': students.objects.all()
    }
    
   return render (request,'students/learners.html',context)