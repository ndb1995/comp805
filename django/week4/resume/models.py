from django.db import models

# Create your models here.
class resume(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def last_name_first_name(self):
        """
        This referes to whatever model object that is being used
        and gets the last name and first name based off the model
        attributes
        """
        return "{}, {}".format(self.last_name, self.first_name)

    def full_name(self):
        """
        This referes to whatever model object that is being used
        and gets the last name and first name based off the model
        attributes. Basically the same as the above method
        but formatted differently
        """
        return "{} {}".format(self.first_name, self.last_name)

    def get_experience(self):
        """
        This method is uses the related manager in python and grabs all
        experience objects that are realted the resume object
        """
        return self.experience_set.all()

    def get_education(self):
        """
        This method is uses the related manager in python and grabs all
        education objects that are realted the resume object
        """
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
