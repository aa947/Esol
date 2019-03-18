from django.db import models
from students.models import students
import random

# Create your models here.
class lession (models.Model):
    
    number_of_students_per_group = models.IntegerField()
    topic = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return ' %s'  %self.topic

pars = students.objects.all()

def group (x, y):
    res=[]
    #N = len(seq)
    for i in range( y):
        while len(res) < y:
            res = random.sample(x,k=y)
            while x[i].first_language == x[i-1].first_language:
                return group(x,y)
    return res

# for i in range(10):
#     pp = group (seq, 2)
#     print(pp)




class Work_groups (models.Model):
    pass