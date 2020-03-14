from django.db import models

# Create your models here.
class FileStore(models.Model):
    fileName = models.CharField(max_length=100,null=False)

class HackAttendDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    gender = models.CharField(max_length=100)
    password = models.CharField(max_length=25)
    fileName = models.ForeignKey(FileStore,on_delete=models.SET_NULL,null=True)