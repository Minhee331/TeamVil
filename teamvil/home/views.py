from django.shortcuts import render
from project.models import *
from account.models import *

# Create your views here.
def home(request):
    projects = Project.objects.all().order_by('-id')[:6]
    profiles = Profile.objects.all().order_by('-id')[:4]
    return render(request, "home.html", {'profiles':profiles, "projects":projects })

def home_back(request):
    projects = Project.objects.all()
    profiles = Profile.objects.all()
    return render(request, "home_back.html", {'profiles':profiles, "projects":projects })
