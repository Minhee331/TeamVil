from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from home.models import *
from account.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_exempt


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
    projects = Project.objects.all().order_by('-register')
    projects_reg = Project.objects.all().order_by('id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "team_search.html", {'projects':projects, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "projects_reg": projects_reg})

def team_search_back_min(request):
    projects = Project.objects.all().order_by('-register')
    projects_reg = Project.objects.all().order_by('id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "team_search_back_min.html", {'projects':projects, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "projects_reg": projects_reg})

def team_search_back_cloud(request):
    projects = Project.objects.all().order_by('-register')
    projects_reg = Project.objects.all().order_by('-id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "team_search_back_cloud.html", {'projects':projects, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "projects_reg": projects_reg})

def team_search_back(request):
    projects = Project.objects.all().order_by('-register')
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
# S타입 팀만들기 html렌더링
def team_new_back_S(request):
    field1 = Field1.objects.all()
    region1 = Region1.objects.all()
    region2 = Region2.objects.all()
    education = Education.objects.all()
    return render(request, 'team_new_back_S.html', {"field1s":field1, "region1s": region1, "region2s": region2, 
                "educations":education })
# C타입 팀만들기 html렌더링
def team_new_back_C(request):
    field1 = Field1.objects.all()
    region1 = Region1.objects.all()
    region2 = Region2.objects.all()
    education = Education.objects.all()
    return render(request, 'team_new_back_C.html', {"field1s":field1, "region1s": region1, "region2s": region2,
                "educations":education })
# P타입 팀만들기 html렌더링
def team_new_back_P(request):
    field1 = Field1.objects.all()
    region1 = Region1.objects.all()
    region2 = Region2.objects.all()
    education = Education.objects.all()
    return render(request, 'team_new_back_P.html', {"field1s":field1, "region1s": region1, "region2s": region2,
                "educations":education })
# S타입 팀 만들기
@csrf_exempt
def team_create_back_S(request):
    if request.method == "POST":  
        title = request.POST['title']
        desc = request.POST['desc']
        field1_id = int(request.POST['field1'])
        field2 = request.POST['field2']
        region1_id = int(request.POST['region1'])
        region2_id = int(request.POST['region2'])
        mem_total = request.POST['mem_total']
        mem_now = request.POST['mem_now']
        duty_name = request.POST['duty_name']
        total = request.POST['total']
        duty_desc = request.POST['duty_desc']
        content = request.POST['content']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        education = int(request.POST['education'])
        project_link = request.POST['project_link'] 
        project = Project()
        if(request.FILES.getlist('project_file')): 
            project.isfile = 1
        project.user_id = request.user
        project.type = 0
        project.title = title
        project.desc = desc
        project.field1_id = Field1.objects.get(id=field1_id)
        project.field2 = field2
        project.region1_id = Region1.objects.get(id=region1_id)
        project.region2_id = Region2.objects.get(id=region2_id)
        project.mem_total = mem_total #프로젝트 총 인원
        project.mem_now = mem_now #모집된 직무 총 인원
        project.start_date = start_date
        project.end_date = end_date
        project.content = content
        if(education!=0):
            project.education_id = Education.objects.get(id=education) #되긴하는데 이게 맞는건가...?
        project.save()
        duty = Duty() # 수정 필요. css 작업 완료되면 for 문으로 바꾸고 여러 duty 저장할 수 있도록
        duty.project_id = project
        duty.total = total
        duty.desc = duty_desc
        duty.name = duty_name
        duty.save()
        project.mem_total = total # 수정 필요 duty 테이블 다 저장하면서 total 누적 시켜야함
        #input file 받아오기
        project.save()
        for files in request.FILES.getlist('project_file'):
            project_file = Project_file()
            project_file.project_id = project
            project_file.file = files
            project_file.save()
            project.isFile = 1
            project.save() 
        if(project_link!=""): # 여러개 입력 가능해지면 수정 필요
            project.isLink = 1
            link = Project_link()
            link.project_id = project
            link.link = project_link
            link.save()
        return redirect('/project/team_detail/' + str(project.id))

# C타입 팀 만들기
def team_create_back_C(request):
    project = Project()
    project.user_id = request.user
    project.use = 0
    project.type = 1
    project.save()
    return redirect('/team_detail/' + str(project.id))
# P타입 팀 만들기
def team_create_back_P(request):
    project = Project()
    project.user_id = request.user
    project.use = 0
    project.type = 2
    project.save()
    return redirect('/team_detail/' + str(project.id))
# 팀 찾기 > 검색 함수
def searchTeam(request):
    obj = json.loads(request.body)
    value = obj['value']
    if value:
        projects = Project.objects.filter(Q(title__icontains = value) | Q(region1_id__region1__icontains=value) | Q(region2_id__region2__icontains=value)
                                        | Q(content__icontains = value) | Q(school__icontains = value) | Q(desc__icontains = value))
        return render(request,'team_list_form.html',{'projects':projects})
    else:
        return render(request,'team_list_form.html')  
 
# 팀 찾기 > 세부 필터링 함수
def filterTeam(request):
    obj = json.loads(request.body)
    field1 = obj['field1']
    region = obj['region']
    state = obj['state']
    if field1[0]=='all':field1=list(Field1.objects.values_list('id', flat=True))
    if region[0]=='all':region=list(Region2.objects.values_list('id', flat=True))
    if state[0]=='all':state=[0, 1]
    projects = Project.objects.filter(field1_id__id__in=field1,region2_id__id__in=region,state__in=state).order_by('id')
    return render(request, "team_list_form.html", {'projects':projects})

#좋아요 만들어지는 함수 create
def like(request):
    obj = json.loads(request.body) #받아온 data를 풀어주기 
    like=Like()
    project_id = Project.objects.get(id=obj['value'])
    like.type = int(0)
    like.project_id = project_id 
    like.from_user_id = request.user
    like.save()
    return render(request,'team_search_back.html')

#좋아요 취소 함수
def likecancel(request):
    obj = json.loads(request.body) #받아온 data를 풀어주기  project_id를 가져올것
    project_id = Project.objects.get(id=obj['value'])
    Like.objects.filter(project_id = project_id).delete() #like모델에 저장된 project_id랑 좋아요를 다시 클릭해서 얻어온 
    return render(request,'team_search_back.html')


# 팀찾기 최신순 정렬 함수
def latestTeam(request):
    projects = Project.objects.all().order_by('-register')
    return render(request, "team_list_form.html", {'projects':projects})

# 지원서 열람 페이지 html 렌더링
def team_application(request):
    return render(request, "team_application.html")

# kay
def team_new(request):
    field1 = Field1.objects.all()
    return render(request, "team_new.html", {"field1s":field1})

def team_form(request):
    return render(request, "team_form.html")

