from django.db import models

# Create your models here.
class experience(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    description = models.TextField()

class education(models.Model):
    institution_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    gpa = models.FloatField()
