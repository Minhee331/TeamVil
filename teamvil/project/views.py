from django.shortcuts import render
from .models import *
from home.models import *
from account.models import *

# Create your views here.
def team_detail(request):
    return render(request, "team_detail.html")

def team_search(request):
    return render(request, "team_search.html")

def team_search_back(request):
    projects = Project.objects.all()
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "team_search_back.html", {'projects':projects, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job})
