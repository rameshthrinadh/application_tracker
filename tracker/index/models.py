from django.db import models

# Create your models here.
class applications(models.Model):
    sid= models.CharField(max_length=7)
    sname= models.CharField(max_length=100)
    semail=models.TextField()
    type=models.TextField()
    message=models.TextField()
    subject=models.TextField()
    step=models.IntegerField()

class admins(models.Model):
    uname=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    desig=models.CharField(max_length=20)
