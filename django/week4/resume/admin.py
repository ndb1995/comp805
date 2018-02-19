from django.contrib import admin
from . models import education, experience, resume


"""
Both of these classes perform the same Function
Instead of going to the admin panel and seeing 'edcuation object'
the attributes of the object will now be rendered
"""
class EducationAdmin(admin.ModelAdmin):
    model = education
    list_display = ('institution_name', 'location', 'degree', 'major', 'gpa')

class ExperienceAdmin(admin.ModelAdmin):
    model = education
    list_display = ('title', 'location', 'start_date', 'end_date', 'description')

class ResumeAdmin(admin.ModelAdmin):
    model = education
    list_display = ('first_name', 'last_name')

# Register your models here.
admin.site.register(education, EducationAdmin)
admin.site.register(experience, ExperienceAdmin)
admin.site.register(resume, ResumeAdmin)
