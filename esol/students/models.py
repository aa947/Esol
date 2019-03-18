from django.db import models

# Create your models here.

class students(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    first_language=models.CharField(max_length=250)
    email= models.EmailField(max_length=70)
    class_type = models.CharField(max_length=250)


    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)