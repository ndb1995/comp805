from django.contrib import admin
from . models import education, experience


class EducationAdmin(admin.ModelAdmin):
    model = education
    list_display = ('institution_name', 'location', 'degree', 'major', 'gpa')

class ExperienceAdmin(admin.ModelAdmin):
    model = education
    list_display = ('title', 'location', 'start_date', 'end_date', 'description')

# Register your models here.
admin.site.register(education, EducationAdmin)
admin.site.register(experience, ExperienceAdmin)
