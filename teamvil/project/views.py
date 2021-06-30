from django.shortcuts import render

# Create your views here.
def team_detail(request):
    return render(request, "team_detail.html")

def team_search(request):
    return render(request, "team_search.html")

def home(request):
    return render(request, "home.html")