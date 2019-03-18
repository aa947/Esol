from django.shortcuts import render
from teacher.models import teacher
from django.db import connection


# Create your views here.

def Home(request):
    return render(request, 'teacher/index.html')




def teacherInfo(request):
    #p =teacher.objects.raw('SELECT * FROM teacher_teacher Where id=1')
    xe = teacher.objects.raw( 'SELECT * FROM teacher_teacher' )
    #pea={}
        # for i in xe:
        #     pe.append(i)
    

    
    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * FROM teacher_teacher Where id=1')
    #     #cursor.execute( 'SELECT * FROM teacher_teacher' )
    #     pea= cursor.fetchall()
    # return pea

    
    #pe = pea[0]
    context = {
        'teachers': xe,
        
        
    }
    return render (request, 'teacher/teacherInfo.html', context)


def teacherProfile(request):
    #p=[]
    context = {
        'profile': teacher.objects.filter(id=1),
        #'para': p 
        }
    return render (request, 'teacher_dtail.html', context)


#     {% for i in x %}
# <h1>  {{  i.class_name  }} {{ i.teacher_name }} </h1>
# {% endfor %}
# {% for i in pe %}
# <p> {{ i }} </p>
# {% endfor %}

def about(request):
    context = {
        'title' : "About"
    }
    return render (request, 'teacher/about.html', context)