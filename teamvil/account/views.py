from django.shortcuts import render
from .models import *
import datetime
# Create your views here.

def member_search_back(request):
    profiles = Profile.objects.all()
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "member_search_back.html", {'profiles':profiles, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job})
