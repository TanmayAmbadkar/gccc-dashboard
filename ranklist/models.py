from django.db import models
from ranklist.get_list import *
from datetime import datetime
from django.utils import timezone
from gcloud import settings

# Create your models here.

class College(models.Model):

    short_name = models.CharField(max_length = 20, primary_key=True)
    long_name = models.CharField(max_length = 200)
    description = models.TextField()
    email = models.EmailField(max_length=100)
    csv = models.FileField(upload_to='csv')
    stamp = models.DateTimeField(blank=True, null=True)
    results = models.BooleanField(default=False)

    def get_results(self):

        execute(self)
        self.stamp = timezone.now()
        self.save()
        print('task finished')

    def __str__(self):

        return self.short_name

class Student(models.Model):

    col = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quests = models.IntegerField(default=0)
    labs = models.IntegerField(default=0)
    url = models.URLField(max_length = 200)
    position = models.IntegerField(default = 1000)
    stamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):

        return self.name


class QuestPosition(models.Model):

    col = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quests = models.IntegerField()
    position = models.IntegerField()

class LabsPosition(models.Model):

    col = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    labs = models.IntegerField()
    position = models.IntegerField()
