from django.shortcuts import render
from .models import *

# Create your views here.
#커뮤니티 리스트 함수
def community(request):
    community = Com.objects.all()
    return render(request,'community_list.html', {'community':community})

def community_detail(request, community_id):
    community = Com.objects.get(id = community_id)
    return render(request, 'community_detail.html', {'community':community})

def community_new(request):
    return render(request, 'community_new.html')
