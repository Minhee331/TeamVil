from django.shortcuts import render
from project.models import *
from account.models import *

# Create your views here.
def home(request):
    return render(request, "home.html")

def home_back(request):
    projects = Project.objects.all()
    profiles = Profile.objects.all()
    return render(request, "home_back.html", {'profiles':profiles, "projects":projects })
