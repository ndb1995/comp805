from django.contrib import admin
from . models import education, experience


class education_model(admin.ModelAdmin):
    model = education
    list_display = ('institution_name', 'location', 'degree', 'major', 'gpa')

# Register your models here.
admin.site.register(education, education_model)
admin.site.register(experience)
