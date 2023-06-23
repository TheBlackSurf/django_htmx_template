from django.shortcuts import render
from django_htmx.http import HttpResponseLocation
# Create your views here.

def index(request):
    if request.htmx:
        return HttpResponseLocation(target="#website-content")
    return render(request, 'index.html')


def aboutPage(request):
    return render(request, 'about-page.html')
        

def contactPage(request):
    return render(request, 'contact-page.html')
        
def homePage(request):
    return render(request, 'home-page.html')
