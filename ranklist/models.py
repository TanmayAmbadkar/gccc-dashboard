from django.db import models
from ranklist.get_list import *
from datetime import datetime
from django.utils import timezone

# Create your models here.

class College(models.Model):

    short_name = models.CharField(max_length = 20, primary_key=True)
    long_name = models.CharField(max_length = 200)
    description = models.TextField()
    email = models.EmailField(max_length=100)
    csv = models.FileField(upload_to='csv')
    results = models.FileField(upload_to='csv', null=True, blank=True)
    stamp = models.DateTimeField(blank=True, null=True)

    def get_results(self):

        results = execute(self.csv)
        results.to_csv(f'csv/{self.short_name}_results.csv')
        self.results = f'csv/{self.short_name}_results.csv'
        self.stamp = timezone.now()
        self.save()
        del results
        print('task finished')

    def __str__(self):

        return self.short_name


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
