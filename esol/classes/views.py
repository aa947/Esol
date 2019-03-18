from django.shortcuts import render
from .models import eng_classes
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def scedule (request):
    # classes = eng_classes.objects.all()
    # for s in classes:
    #     participants= s.students_enrolled.all()
    

    
        
    context= {
        'clax': eng_classes.objects.all(),
        #'prax': participants,

    }
    return render(request, 'classes/classes_scedule.html', context)
