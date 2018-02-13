from django.shortcuts import render
from . models import education, experience
# Create your views here.
def display_experience_education(request):
    """
    This will render the updated resume page.
    All the original content has been removed
    and replace with querysets from the database.
    You can only pass context as dictionaries
    Later in the html page, we will use a for loop
    to loop through the dictionaries and display the data
    """
    all_education = education.objects.all()
    all_experience = experience.objects.all()
    context = {'all_education': all_education,'all_experience': all_experience,}
    return render(request, 'resume.html', context)
