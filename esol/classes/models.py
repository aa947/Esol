from django.db import models
from teacher.models import teacher
from students.models import students

# Create your models here.
class eng_classes (models.Model,):
    class_time = models.CharField( max_length = 250)
    class_teacher = models.ForeignKey(teacher, on_delete = models.CASCADE)
    students_enrolled= models.ManyToManyField(students, related_name='participants')

    def __str__(self):
        return '%s %s' %(self.class_time, self.class_teacher)