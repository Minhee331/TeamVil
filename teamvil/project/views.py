from typing import Text
from django.db.models.fields import DateTimeField
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from home.models import *
from account.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q, Case
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count

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
    projects_reg = Project.objects.all().order_by('id')[:4]
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
    region1 = Region1.objects.all() #서울시 경기도 충청도 등등의 첫번째 도 
    region1_list = {} #{'서울시' '경기도 --'}
    region2_list = []
    region_list = {}
    for prov in region1:
        region2_list = Region2.objects.filter(region1_id = prov) #{'서울시 서초구','서울시 강남구','서울시 중구'}
        region1_list[prov.region1] = region2_list
        li = []
        for r in region2_list: 
            li.append([r.id, r.region2]) #['0','서초구'] // ['1','강남구'] 
        region_list[prov.region1] = li #region_list['서울시'] = ['0','서초구']
    #   region1_list['서울시'] = ['강남구', '중구', '서초구']
    #   region1_list['경기도'] = ['고양시', '안산시', '용인시']
    #   item으로 뽑으면 key랑 value모두 뽑힘 -> [('서울시',['강남구','중구','서초구'])]
    #region2 = Region2.objects.all()
    education = Education.objects.all()
    return render(request, 'team_new_back_S.html', {"field1s":field1, "region1s": region1, "region1_list": region1_list.items(), "region_list":region_list #"region2s": region2, 
                            , "educations":education })
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
        school = request.POST['school']
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
        project.school = school
        if(education!=0):
            project.education_id = Education.objects.get(id=education)
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
    projects = Project.objects.filter(field1_id__id__in=field1,region2_id__id__in=region,state__in=state).order_by('-id')
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
    #알람기능 추가
    profile = Profile.objects.get(user_id=request.user)
    alarm=Alarm()
    alarm.type = int(1)
    alarm.user_id = project_id.user_id
    alarm.like_id = like
    alarm.member_url = '/member/member_detail/' + str(profile.id)
    alarm.project_url = '/project/team_detail/' + str(project_id.id) #프로젝트 연결도 추가시켜주는게 좋을 것 같다.
    alarm.save()
    return render(request,'team_search_back.html') #team_list에도 적용이 되야된다


#좋아요 취소 함수
def likecancel(request):
    obj = json.loads(request.body) #받아온 data를 풀어주기  project_id를 가져올것
    project_id = Project.objects.get(id=obj['value'])
    Like.objects.get(project_id = project_id, from_user_id = request.user).delete() #like모델에 저장된 project_id랑 좋아요를 다시 클릭해서 얻어온 
    return render(request,'team_search_back.html')


# 팀찾기 최신순 정렬 함수
def latestTeam(request):
    obj = json.loads(request.body)
    field1 = obj['field1']
    region = obj['region']
    state = obj['state']
    if field1[0]=='all':field1=list(Field1.objects.values_list('id', flat=True))
    if region[0]=='all':region=list(Region2.objects.values_list('id', flat=True))
    if state[0]=='all':state=[0, 1]
    projects = Project.objects.filter(field1_id__id__in=field1,region2_id__id__in=region,state__in=state).order_by('-id')
    return render(request, "team_list_form.html", {'projects':projects})

# 팀찾기 인기순 정렬 함수
def popularTeam(request):
    obj = json.loads(request.body)
    field1 = obj['field1']
    region = obj['region']
    state = obj['state']
    if field1[0]=='all':field1=list(Field1.objects.values_list('id', flat=True))
    if region[0]=='all':region=list(Region2.objects.values_list('id', flat=True))
    if state[0]=='all':state=[0, 1]
    projects = Project.objects.filter(field1_id__id__in=field1,region2_id__id__in=region,state__in=state).order_by('-id')
    like = Like.objects.filter(type = 0, project_id__in = projects).values('project_id').annotate(cnt = Count('project_id')).order_by('-cnt')
    like_list = list(like)
    like_id = [d['project_id'] for d in like_list]
    projects = []
    for i in like_id:
        p = Project.objects.get(id =i)
        projects.append(p)
    not_like_projects = Project.objects.filter(field1_id__id__in=field1,region2_id__id__in=region,state__in=state).exclude(id__in=like_id).order_by('-id')
    return render(request, "team_list_form.html", {'projects':projects, "not_like_projects":not_like_projects})

# 지원서 열람 페이지 html 렌더링
def team_application(request):
    return render(request, "team_application.html")

# 팀원 리뷰 페이지 html 렌더링
def team_review(request, project_id):
    user = request.user
    project = Project.objects.get(id=project_id)
    members = Member.objects.filter(~Q(user_id=user), project_id=project_id, register_state=1)
    member_user_ids = [member.user_id for member in members]
    profiles = Profile.objects.filter(user_id__in=member_user_ids)
    duties = Duty.objects.filter()
    return render(request, "team_review.html", {'project':project, 'profiles':profiles, 'duties':duties,
                "members":members})

# 팀원 리뷰 입력 함수
@csrf_exempt
def team_review_form(request):
    if request.method == "POST": 
        print(123)
        obj = json.loads(request.body)
        print(obj)
        id_list = obj['id_list']
        content_list = obj['content_list']
        rating_list = obj['rating_list']
        project_id = obj['project_id']
        project = Project.objects.get(id = project_id)
        for i in range(len(id_list)):
            review = User_review()
            to_user = Member.objects.get(id = id_list[i])
            review.from_user_id = request.user
            review.to_user_id = to_user.user_id
            review.project_id = project
            review.content =  content_list[i]
            review.total = rating_list[i]
            review.save()
    # project = Project.objects.get()
    # if request.method == "POST": 
    #     total = request.POST['total']
    #     content = request.POST['content']
    #     to_user_id = request.POST['to_user_id']
    #     user_review = User_review()
    #     user_review.from_user_id = request.user
    #     user_review.to_user_id = to_user_id
    #     user_review.project_id = request.project_id
    #     user_review.total = total
    #     user_review.content = content
    #     user_review.save()
    # for total in request.POST.getlist('total'):
    #     member_review = User_review()
    #     member_review.project_id = project
    #     member_review.total = total
    #     member_review.save()
    # for content in request.POST.getlist('content'):
    #     member_review = User_review()
    #     member_review.project_id = project
    #     member_review.content = content
    #     member_review.save()
        return redirect('/project/team_detail/' + str(project_id))
    # return ""


# kay
def team_new(request):
    if request.method == "POST":
        obj = json.loads(request.body)
        type = obj['type']
        title = obj['title']
        desc = obj['desc']
        field1_id = Field1.objects.get(id = int(obj['field1_id']))
        filed2 = obj['filed2']
        region1_id = Region1.objects.get(id = int(obj['region1_id']))
        region2_id = Region2.objects.get(id = int(obj['region2_id']))
        mem_total = obj['mem_total']
        mem_now = obj['mem_now']
        mem_duty = obj['mem_duty']
        content = obj['content']
        start_date = obj['start_date']
        end_date = obj['end_date']
        school = obj['school']
        link = obj['link']
        education_id = int(obj['education_id'])
        if education_id!= 0 : education_id = Education.objects.get(id=education_id)
        duty_list = obj['duty_list']
        duty_desc = obj['duty_desc']
        q_list = obj['q_list']
        # 프로젝트 저장 시작
        # todo . 대표사진 모델 생성 필요
        project = Project()
        project.user_id = request.user
        project.type = int(type)
        project.title = title
        project.desc = desc
        project.field1_id = field1_id
        project.field2 = filed2
        project.region1_id = region1_id
        project.region2_id = region2_id
        project.mem_total = mem_total
        project.mem_now = mem_now
        project.mem_duty = mem_duty
        project.start_date = start_date
        project.end_date = end_date
        if school!="": project.school = school
        project.content = content
        if link!="": 
            project.isLink = 1
        if education_id != 0: project.education_id = education_id
        project.save()
        # 프로젝트 저장 끝
        # 링크 저장 시작
        if link!="": 
            db_link = Project_link()
            db_link.project_id = project
            db_link.link = link
            db_link.save()
        # 링크 저장 끝
        # todo . 파일 저장 구현 필요
        for d in duty_list:
            duty = Duty()
            duty.project_id = project
            duty.total = d[1]
            duty.desc = duty_desc
            # todo . desc 직무마다 구현 필요
            duty.name = d[0]
            duty.save()
        apply = Apply_form()
        qi_list = []
        # Question 저장시작
        for q in q_list:
            question = Question()
            question.project_id = project
            if(q['type']==0):
                question.type = 0
                question.isRequired = 1
                question.content = q['content']
                choice_list = q['choice_list']
                for i in range(0,len(q['choice_list'])):
                    if i==0:
                        question.choice1 = q['choice_list'][i]
                    if i==1:
                        question.choice2 = q['choice_list'][i]
                    if i==2:
                        question.choice3 = q['choice_list'][i]
                    if i==3:
                        question.choice4 = q['choice_list'][i]
                    if i==4:
                        question.choice5 = q['choice_list'][i]
            else:
                question.type = q['type']
                question.isRequired = 1
                question.content = q['content']
            question.save()
            qi_list.append(question)
        # Question 저장 끝
        # Apply_form 저장 시작
        apply.project_id = project
        apply.user_id = request.user
        for i in range(0,len(qi_list)):
            if i==0:
                apply.q1_id = qi_list[i]
            if i==1:
                apply.q2_id = qi_list[i]
            if i==2:
                apply.q3_id = qi_list[i]
            if i==3:
                apply.q4_id = qi_list[i]
            if i==4:
                apply.q5_id = qi_list[i]
            if i==5:
                apply.q6_id = qi_list[i]
            if i==6:
                apply.q7_id = qi_list[i]
            if i==7:
                apply.q8_id = qi_list[i]
            if i==8:
                apply.q9_id = qi_list[i]
            if i==9:
                apply.q10_id = qi_list[i]
        apply.save()
        # Apply_form 저장 끝
        essence = {
        'project_id':project.id
        }
        return JsonResponse(essence)
    else:
        field1 = Field1.objects.all()
        region1 = Region1.objects.all() #서울시 경기도 충청도 등등의 첫번째 도 
        region1_list = {} #{'서울시' '경기도 --'}
        region2_list = []
        region_list = {}
        for prov in region1:
            region2_list = Region2.objects.filter(region1_id = prov) #{'서울시 서초구','서울시 강남구','서울시 중구'}
            region1_list[prov.region1] = region2_list
            li = []
            for r in region2_list: 
                li.append([r.id, r.region2]) #['0','서초구'] // ['1','강남구'] 
            region_list[prov.region1] = li #region_list['서울시'] = ['0','서초구']
        education = Education.objects.all()
        return render(request, "team_new.html", {"field1s":field1, "region1s": region1, "region1_list": region1_list.items(), "region_list":region_list, "educations":education})


def team_form(request):
    return render(request, "team_form.html")

# 지원서 작성 폼
@csrf_exempt
def  question_form(request,project_id):
    if request.method == "POST": # 저장 
        user = request.user
        project = Project.objects.get(id = project_id)
        q1 = Question()
        q2 = Question()
        q3 = Question()
        type1= int(request.POST['q_type_1'])
        type2= int(request.POST['q_type_2'])
        type3= int(request.POST['q_type_3'])
        if(type1 == 0):
            q1.project_id = project
            q1.type = 0
            if(request.POST['isRequired_1']=='0'):
                q1.isRequired = 0
            else:
                q1.isRequired = 1
            content_1 = request.POST['content_1']
            choice_cnt=request.POST['choice_cnt']
            choice1 = request.POST['choice1']
            choice2 = request.POST['choice2']
            choice3 = request.POST['choice3']
            choice4 = request.POST['choice4']
            choice5 = request.POST['choice5'] 
            q1.content=content_1
            q1.choice_cnt=choice_cnt
            q1.choice1=choice1
            q1.choice2=choice2
            q1.choice3=choice3
            q1.choice4=choice4
            q1.choice5=choice5
            q1.save()
        if(type2 == 1):
            q2.project_id = project
            q2.type = 1
            if(request.POST['isRequired_2']=='0'):
                q2.isRequired = 0
            else:
                q2.isRequired = 1
            content_2 = request.POST['content_2']
            q2.content=content_2
            q2.save()
        if(type3 == 2):
            q3.project_id = project
            q3.type = 2
            if(request.POST['isRequired_3']=='0'):
                q3.isRequired = 0
            else:
                q3.isRequired = 1
            content_3 = request.POST['content_3']
            q3.content=content_3
            q3.save()           
        apply_form =Apply_form()
        user = request.user
        apply_form.project_id =project
        apply_form.user_id =user
        apply_form.q1_id = q1
        apply_form.q2_id = q2
        apply_form.q3_id = q3
        apply_form.save()
        return redirect('/')
    else: # 페이지 불러올 때
        return render(request,"team_apply_form_back.html",{"project_id":project_id})


        
   
     

#팀지원서 양식 폼
@csrf_exempt
def team_apply(request,project_id):
    if request.method == "POST":
        obj = json.loads(request.body)
        duty_id = obj['duty_id']
        a_list = obj['a_list']
        ai_list = []
        for a in a_list:
            answer = Answer()
            question_id = Question.objects.get(id = a['q_id'])
            answer.question_id = question_id
            answer.type = a['q_type']
            if a['q_type']==0:
                answer.choice_answer = a['choice_answer']
                answer.choice_text = a['choice_text']
            elif a['q_type']==1:
                answer.short_answer = a['short_answer']
            elif a['q_type']==2:
                answer.long_answer = a['long_answer']
            answer.save()
            ai_list.append(answer)
        application = Application()
        project = Project.objects.get(id = int(project_id))
        application.project_id = project
        application.user_id = request.user
        for i in range(0,len(ai_list)):
            if i==0:
                application.a1_id = ai_list[i]
            if i==1:
                application.a2_id = ai_list[i]
            if i==2:
                application.a3_id = ai_list[i]
            if i==3:
                application.a4_id = ai_list[i]
            if i==4:
                application.a5_id = ai_list[i]
            if i==5:
                application.a6_id = ai_list[i]
            if i==6:
                application.a7_id = ai_list[i]
            if i==7:
                application.a8_id = ai_list[i]
            if i==8:
                application.a9_id = ai_list[i]
            if i==9:
                application.a10_id = ai_list[i]
        application.state = 0
        application.save()
        essence = {
            'project_id':project.id
        }
        return JsonResponse(essence)
    else:
        project = Project.objects.get(id=project_id)
        profile = Profile.objects.get(user_id = project.user_id)
        duties = Duty.objects.filter(project_id = project_id)
        question = Question.objects.filter(project_id = project)
        questiondict = {} 
        for question in question:
            questionlist = []
            questions = Question.objects.filter(project_id = project)
            for question in questions:
                questionlist.append(question)
            questiondict[str(question.id)] = questionlist
        return render(request,"team_apply.html",{"question":question,"project_id":project_id,"project":project,"profile":profile,"duties":duties,"questiondict":questiondict.items()})


@csrf_exempt
def answer_form(request,project_id):
    if request.method == "POST":
        obj = json.loads(request.body)
        q1 = obj['q1']
        q2 = obj['q2']
        q3 = obj['q3'] # ([0, choice_answer, choice_text])
        # q1[0]
        # q2 = obj['short']
        # q3 = obj['long']
        # if q1[0] == 0 :
        #     q = Question.objects.get(id = q1[1])
        #     ans = Answer()
        #     # 객관식 답 저장
        # if q2[0] == 1:
        #     ans = Answer()
        #     # 단답식 답 저장 
        # project = Project.objects.get(id=project_id)
        # question = Question.objects.filter(project_id = project)
        answer = Answer()
        answer.q1=q1
        # answer.q1=q2
        # answer.q1=q3
        answer.save()
            #이 다음부터는 아직 못채우겠어요...
        return redirect('/project/team_answer_form_back_sunneng/' + str(project_id))
        
        
        
    

        



#스크랩 함수
def scrap(request):
    obj = json.loads(request.body)
    scrap=Scrap()
    project_id = Project.objects.get(id=obj['value'])
    scrap.type = int(0)
    scrap.project_id = project_id
    scrap.from_user_id = request.user
    scrap.save()
    #알람기능 추가
    profile = Profile.objects.get(user_id=request.user)
    alarm=Alarm()
    alarm.type = int(3)
    alarm.user_id = project_id.user_id
    alarm.scrap_id = scrap
    alarm.member_url = '/member/member_detail/' + str(profile.id)
    alarm.project_url = '/project/team_detail/' + str(project_id.id) #프로젝트 연결도 추가시켜주는게 좋을 것 같다.
    alarm.save()
    return render(request,'team_search_back.html')


#스크랩 취소 함수
def scrapcancel(request):
    obj = json.loads(request.body)
    project_id = Project.objects.get(id=obj['value'])
    Scrap.objects.get(project_id = project_id, from_user_id = request.user).delete()
    return render(request,'team_search_back.html')



#학교검색 함수

    
  






