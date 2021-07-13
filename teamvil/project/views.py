from django.shortcuts import redirect, render
from .models import *
from home.models import *
from account.models import *
# from django.contrib.auth.models import User
# from django.contrib import auth
from django.utils import timezone


# Create your views here.
def team_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    profile = Profile.objects.get(user_id = project.user_id)
    project_links = Project_link.objects.filter(project_id = project_id)
    project_files = Project_file.objects.filter(project_id = project_id)
    duties = Duty.objects.filter(project_id = project_id)
    return render(request, "team_detail.html", {'project':project, 'profile':profile, 
                "project_links":project_links, "project_files":project_files, "duties": duties})

def team_search(request):
    projects = Project.objects.all()
    projects_reg = Project.objects.all().order_by('id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "team_search.html", {'projects':projects, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "projects_reg": projects_reg})

def team_search_back(request):
    projects = Project.objects.all()
    projects_reg = Project.objects.all().order_by('id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "team_search_back.html", {'projects':projects, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "projects_reg": projects_reg})

def team_detail_back(request, project_id):
    project = Project.objects.get(id=project_id)
    profile = Profile.objects.get(user_id = project.user_id)
    project_links = Project_link.objects.filter(project_id = project_id)
    project_files = Project_file.objects.filter(project_id = project_id)
    duties = Duty.objects.filter(project_id = project_id)
    return render(request, "team_detail_back.html", {'project':project, 'profile':profile, 
                "project_links":project_links, "project_files":project_files, "duties": duties})

def team_new_back_S(request):
    return render(request, 'team_new_back_S.html')

def team_new_back_C(request):
    return render(request, 'team_new_back_C.html')

def team_new_back_P(request):
    return render(request, 'team_new_back_P.html')

def team_create_back_S(request):
    project = Project()
    project.user_id = request.user
    project.use = 0
    project.isEnd = 0
    project.type = 0
    project.title = request.GET['title']
    project.desc = request.GET['desc']
    field1 = Field1.objects.all()
    region2 = Region2.objects.all()
    project.field1_id = 1
    project.field2_id = request.GET['field2_id']
    # project.mem_total = ?
    # project.mem_duty_name = request.GET['mem_duty_name']
    # project.mem_duty = 
    project.mem_now = request.GET['field2_id']
    project.save()
    return redirect('/team_detail/' + str(project.id))

def team_create_back_C(request):
    project = Project()
    project.user_id = request.user
    project.use = 0
    project.type = 1
    project.save()
    return redirect('/team_detail/' + str(project.id))

def team_create_back_P(request):
    project = Project()
    project.user_id = request.user
    project.use = 0
    project.type = 2
    project.save()
    return redirect('/team_detail/' + str(project.id))


