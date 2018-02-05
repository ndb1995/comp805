from django.shortcuts import render

def home(request):
    """
    Renders the home page
    """
    context = {}
    return render(request, 'home.html', context)

def resume(request):
    """
    Renders the home page
    """
    context = {}
    return render(request, 'resume.html', context)

def portfolio(request):
    """
    Renders the home page
    """
    context = {}
    return render(request, 'portfolio.html', context)

def contact(request):
    """
    Renders the home page
    """
    context = {}
    return render(request, 'contact.html', context)
