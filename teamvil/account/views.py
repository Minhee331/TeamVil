from django.shortcuts import render
from .models import *
import datetime
# Create your views here.

def member_search_back(request):
    profiles = Profile.objects.all()
    return render(request, "member_search_back.html", {'profiles':profiles})
