from django.db import models
from django.contrib.auth.models import User
import datetime

class remainders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title",max_length=50)
    task = models.CharField(verbose_name="Name of task",max_length=300)
    date = models.DateField(verbose_name="Date of reminder")
    timer = models.TimeField(verbose_name="Time of reminder")
    share = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def getdata(self,name):
        print(self.name)
        return self.name