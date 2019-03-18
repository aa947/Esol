from django.db import models

# Create your models here.
class teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    teacher_email = models.EmailField(max_length=70)



    def __str__(self):
        return '%s' %self.teacher_name





    