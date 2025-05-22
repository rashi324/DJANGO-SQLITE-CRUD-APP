
# Create your models here.
from django.db import models


class Employee(models.Model):
    empid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=30,null=True)
    desg=models.CharField(max_length=30,null=True)
    salary=models.FloatField(null=True)
    image=models.FileField(upload_to='profile',null=True)
    def __str__(self):
        return (self.ename)