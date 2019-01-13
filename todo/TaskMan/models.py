from django.db import models
import datetime
# Create your models here.
'''
class List(models.Model):
    Task = models.CharField(max_length=300)
    completed = models.BooleanField(default= False)
    Deadline = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=90))

    def __str__(self):
        return str(self.Task) + ' | ' + str(self.completed)

'''

class todo(models.Model):
    Task = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    Deadline = models.DateTimeField(default=datetime.datetime.now()+ datetime.timedelta(days=90))

    def __str__(self):
        return str(self.Task) + ' | ' + str(self.completed) + ' | ' + str(self.Deadline)