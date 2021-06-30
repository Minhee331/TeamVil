from django.shortcuts import render

# Create your views here.
def team_detail(request):
    return render(request, "team_detail.html")