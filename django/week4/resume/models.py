from django.db import models

# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def last_name_first(self):
        return "{} {}".format(self.last_name, self.first_name)

class experience(models.Model):
    parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
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
