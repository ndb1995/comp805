from django.shortcuts import render
from . models import education, experience, resume
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

    resume_object = resume.objects.get(pk=1)
    context = {'resume_object':resume_object}
    return render(request, 'resume.html', context)
