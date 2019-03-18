from django.shortcuts import render
from students.models import students
from .models import lession
import random
from .funcs import groupp
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def lession_c (request):
    context = {
        'lessions': lession.objects.all()
    }
    return render (request, 'lessions/lessions.html', context) 

@login_required
def lession_group (request):
    results=[]
    parr = list(students.objects.all())
    pick = []
    picked = []
    final = []
    for i in range(4):
        pick = groupp (parr, 2)
        while pick in final or pick[::-1] in final or any(p in picked for p in pick):
            pick = groupp (parr, 2)
        final.append(pick)
        picked.extend(pick)

    context = {
        'grous': final,
    }
    return render (request, 'lessions/groups.html', context)