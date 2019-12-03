from django.db import models

# Create your models here.
class student(models.Model):
    rollno=models.CharField(max_length=100)
    name=models.CharField(max_length=500)
    course=models.CharField(max_length=50)
    year=models.IntegerField(default=0)
    gtname=models.CharField(max_length=500)

    def __str__(self):
       return self.name
# Create your models here.
