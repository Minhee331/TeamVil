from django.shortcuts import render
from .models import *
# Create your views here.
def team_detail(request):
    return render(request, "team_detail.html")

def team_search(request):
    return render(request, "team_search.html")

def team_search_back(request):
    projects = Project.objects.all()
    return render(request, "team_search_back.html", {'projects':projects})
