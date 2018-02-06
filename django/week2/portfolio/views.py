from django.shortcuts import render

def home(request):
    """
    Renders the home page
    """
    context = {}
    return render(request, 'home.html', context)

def resume(request):
    """
    Renders the resume page
    """
    context = {}
    return render(request, 'resume.html', context)

def portfolio(request):
    """
    Renders the portfolio page
    """
    context = {}
    return render(request, 'portfolio.html', context)

def contact(request):
    """
    Renders the contact page
    """
    context = {}
    return render(request, 'contact.html', context)
