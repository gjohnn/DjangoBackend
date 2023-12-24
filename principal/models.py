from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

class Tasks(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    title = models.CharField(max_length=100)