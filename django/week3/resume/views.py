from django.shortcuts import render

# Create your views here.
def education(request):
    """
    Renders the home page
    """
    context = {}
    return render(request, 'education.html', context)

def experience(request):
    """
    Renders the home page
    """
    context = {}
    return render(request, 'experience.html', context)
