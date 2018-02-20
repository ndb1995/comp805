from django.shortcuts import render
from . models import education, experience, resume
# Create your views here.
def display_experience_education(request):
    """
    This will send the first resume object to
    resume.html, where it will be displayed
    """

    resume_object = resume.objects.first()
    context = {'resume_object':resume_object}
    return render(request, 'resume.html', context)
