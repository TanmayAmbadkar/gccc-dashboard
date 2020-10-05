from django.db import models
from ranklist.get_list import *

# Create your models here.

class College(models.Model):

    short_name = models.CharField(max_length = 20)
    long_name = models.CharField(max_length = 200)
    description = models.TextField()
    email = models.EmailField(max_length=100)
    csv = models.FileField(upload_to='csv')

    def get_results(self):

        return  execute(self.csv)

class QuestPosition(models.Model):

    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quests = models.IntegerField()
    position = models.IntegerField()

class LabsPosition(models.Model):

    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    labs = models.IntegerField()
    position = models.IntegerField()
