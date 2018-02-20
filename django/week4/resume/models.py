from django.db import models

# Create your models here.
class resume(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def last_name_first_name(self):
        return "{}, {}".format(self.last_name, self.first_name)

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_experience(self):
        return self.experience_set.all()

    def get_education(self):
        return self.education_set.all()

class experience(models.Model):
    parent_resume = models.ForeignKey('resume', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    description = models.TextField()

class education(models.Model):
    parent_resume = models.ForeignKey('resume', on_delete=models.CASCADE, default=1)
    institution_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    gpa = models.FloatField()
