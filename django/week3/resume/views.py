from django.shortcuts import render
from . models import education, experience
# Create your views here.
def education_view(request):
    """
    Renders the home page
    """
    all_education = education.objects.all()
    context = {}
    return render(request, 'education.html', {'all_education': all_education,})

def experience_view(request):
    """
    Renders the home page
    """
    all_experience = experience.objects.all()
    context = {}
    return render(request, 'experience.html', {'all_experience': all_experience,})
