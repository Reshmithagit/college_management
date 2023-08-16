from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Addcourse(models.Model):
    coursename=models.CharField(max_length=255)
    coursefee=models.IntegerField(null=True)
class Student(models.Model):
    course=models.ForeignKey(Addcourse,on_delete=models.CASCADE,null=True)
    stdname=models.CharField(max_length=255)
    Address=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    date=models.DateField()

class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Addcourse,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    contact=models.CharField(max_length=255)
    img=models.ImageField(blank=True,upload_to="image/",null=True)
