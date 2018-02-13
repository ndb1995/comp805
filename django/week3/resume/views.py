from django.shortcuts import render
from . models import education, experience
# Create your views here.
def display_experience_education(request):
    """
    Renders the home page
    """
    all_education = education.objects.all()
    all_experience = experience.objects.all()
    context = {'all_education': all_education,'all_experience': all_experience,}
    return render(request, 'resume.html', context)
