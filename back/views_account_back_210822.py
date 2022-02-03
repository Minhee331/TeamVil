from typing import ContextManager
from django.db.models.query_utils import PathInfo
from django.shortcuts import render , redirect
from .models import *
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from django.conf import settings
from django.db.models import Q
from project.models import *
from home.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.db.models import Avg, Count
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
import os
import sys
import urllib.request
from django.core.files.storage import FileSystemStorage

def callback(request):
    return render(request, 'callback.html')
    
def member_search(request):
    profiles = Profile.objects.all().order_by('-register')
    # profiles_reg = Profile.objects.all().order_by('-id')[:4]
    user = request.user
    profile = Profile.objects.get(user_id = user)
    if profile.mbti_id.mbti == 'ENTP': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 10) | Q(mbti_id = 12)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ISFJ': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 10) | Q(mbti_id = 2)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ESFJ': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 2) | Q(mbti_id = 4)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'INTP': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 12) | Q(mbti_id = 10)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ENFJ': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 13) | Q(mbti_id = 15)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ISTP': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 7) | Q(mbti_id = 5)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ESTP': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 5) | Q(mbti_id = 7)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'INFJ': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 15) | Q(mbti_id = 13)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ESFP': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 1) | Q(mbti_id = 3)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'INTJ': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 16) | Q(mbti_id = 14)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ENTJ': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 14) | Q(mbti_id = 16)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ISFP': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 3) | Q(mbti_id = 1)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ESTJ': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 6) | Q(mbti_id = 8)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'INFP': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 11) | Q(mbti_id = 9)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ENFP': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 9) | Q(mbti_id = 11)).order_by('-view_cnt')[:8]
    elif profile.mbti_id.mbti == 'ISTJ': 
        profiles_reg = Profile.objects.filter(Q(mbti_id = 8) | Q(mbti_id = 6)).order_by('-view_cnt')[:8]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    page_len = len(profiles)//18
    if len(profiles)%18 != 0:
        page_len+=1
    page = list(range(1, page_len+1))
    profiles = profiles[0:18]
    return render(request, "member_search.html", {'profiles':profiles, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "profiles_reg":profiles_reg, "page": page, "current_page":1})


def member_search_back(request):
    profiles = Profile.objects.all().order_by('-register')
    profiles_reg = Profile.objects.all().order_by('id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "member_search_back.html", {'profiles':profiles, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "profiles_reg":profiles_reg})

#팀원찾기페이지 - 클라우드
def member_search_back_cloud(request):
    profiles = Profile.objects.all().order_by('-register')
    profiles_reg = Profile.objects.all().order_by('id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "member_search_back_cloud.html", {'profiles':profiles, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "profiles_reg":profiles_reg})

def member_detail(request, profile_id):
    profile = Profile.objects.get(id = profile_id)
    carrers = User_carrer.objects.filter(user_id = profile.user_id)
    user_links = User_link.objects.filter(user_id = profile.user_id)
    user_files = User_file.objects.filter(user_id = profile.user_id)
    user_review = User_review.objects.filter(to_user_id = profile.user_id).order_by('-id')
    user_review_avg = User_review.objects.filter(to_user_id = profile.user_id).aggregate(Avg('total'))
    user_review_cnt = len(User_review.objects.filter(to_user_id = profile.user_id))
    # q = User_review.objects.filter(to_user_id = profile.user_id).annotate(Count('total'))
    # user_review_cn = q[0].total__count
    user_review_1 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 1))
    user_review_2 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 2))
    user_review_3 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 3))
    user_review_4 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 4))
    user_review_5 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 5))
    print(user_review)
    # print(user_review_cnt)
    # print(user_review_cn)
    profile.view_cnt +=1
    profile.save()
    user_review_all = [user_review_1, user_review_2, user_review_3, user_review_4, user_review_5]
    return render(request, "member_detail.html", {"profile":profile, "carrers":carrers,
                "user_review": user_review, "user_links": user_links, "user_files": user_files, "user_review_all": user_review_all, "user_review_avg": user_review_avg, "user_review_cnt": user_review_cnt })

def member_detail_back(request, profile_id):
    profile = Profile.objects.get(id = profile_id)
    carrers = User_carrer.objects.filter(user_id = profile.user_id)
    user_links = User_link.objects.filter(user_id = profile.user_id)
    user_files = User_file.objects.filter(user_id = profile.user_id)
    return render(request, "member_detail_back.html", {"profile":profile, "carrers":carrers,
                "user_links": user_links, "user_files": user_files})

def member_detail_back_min(request, profile_id):
    profile = Profile.objects.get(id = profile_id)
    carrers = User_carrer.objects.filter(user_id = profile.user_id)
    user_links = User_link.objects.filter(user_id = profile.user_id)
    user_files = User_file.objects.filter(user_id = profile.user_id)
    return render(request, "member_detail_back_min.html", {"profile":profile, "carrers":carrers,
                "user_links": user_links, "user_files": user_files})

# 회원가입 함수
def signup(request):
    if request.method == "POST":   
        username = request.POST['username']
        password = request.POST['password']
        passwordCheck = request.POST['passwordCheck']
        name = request.POST['name']
        phone = request.POST['phone']
        if not (username and password and passwordCheck and name and phone) :
            return render(request, 'signup.html', {'error':"모든 값을 입력해주세요."})
        elif User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error':"이미 존재하는 아이디입니다."})
        elif Profile.objects.filter(phone = phone).exists():
            return render(request, "signup.html", {'error': '이미 등록된 연락처입니다.'})
        elif type(name) != str:                     #이거 안돼요
            return render(request, "signup.html", {'error': '이름을 다시 입력해주세요.'})
        elif len(name) >6:
            return render(request, "signup.html", {'error': '이름을 다시 입력해주세요.'}) 
        elif len(phone) !=11:
            return render(request, "signup.html", {'error': '핸드폰 번호 11자리를 다시 입력해주세요.'})  
        elif password != passwordCheck :
            return render(request, "signup.html", {'error': '비밀번호가 일치하지 않습니다.'})     
        else:
            user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
            profile = Profile()
            profile.user_id = user
            profile.name = name
            mbti = Mbti.objects.get(id=1)
            profile.mbti_id =  mbti# 추후 수정 필요
            mbti.mbti_cnt = mbti.mbti_cnt + 1
            mbti.save()
            profile.email = "email" # 추후 수정 필요
            profile.phone =  phone
            profile.birthday = "1999-07-10" # 추후 수정 필요
            profile.region1_id = Region1.objects.get(id=1) # 추후 수정 필요
            profile.region2_id = Region2.objects.get(id=1) # 추후 수정 필요
            profile.openPhone = 0
            profile.openEmail = 0 
            profile.term_id =  Term.objects.get(id=1) # 추후 수정 필요
            profile.field1_id = Field1.objects.get(id=1) # 추후 수정 필요
            profile.field2 = "Field2" # 추후 수정 필요
            profile.state = 1 
            profile.job_id =  Job.objects.get(id=1) # 추후 수정 필요
            profile.isLink = 0
            profile.isFile =0
            profile.isCarrer = 0 
            profile.isReview = 0
            profile.save()
            auth.login(request, user)
            return redirect('/')
    else :
        return render(request, 'signup.html')

def signup_k(request):
    if request.method == "POST": 
        obj = json.loads(request.body)  
        user_name= obj['name']
        user_id = obj['id']
        if User.objects.filter(username=user_id).exists():
            user = authenticate(request, username=user_id, password='0000')
            auth.login(request,user)
            return render(request, 'signup.html')   
        else:
            print('kakao')
            print(obj)
            user = User.objects.create_user(username=user_id, password='0000')
            profile = Profile()
            profile.user_id = user
            profile.name = user_name
            mbti = Mbti.objects.get(id=1)
            profile.mbti_id =  mbti# 추후 수정 필요
            mbti.mbti_cnt = mbti.mbti_cnt + 1
            mbti.save()
            profile.email = "email" # 추후 수정 필요
            profile.phone =  "010-1234-5678"
            profile.birthday = "2021-07-10" # 추후 수정 필요
            profile.region1_id = Region1.objects.get(id=1) # 추후 수정 필요
            profile.region2_id = Region2.objects.get(id=1) # 추후 수정 필요
            profile.openPhone = 0
            profile.openEmail = 0 
            profile.term_id =  Term.objects.get(id=1) # 추후 수정 필요
            profile.field1_id = Field1.objects.get(id=1) # 추후 수정 필요
            profile.field2 = "Field2" # 추후 수정 필요
            profile.state = 1 
            profile.job_id =  Job.objects.get(id=1) # 추후 수정 필요
            profile.isLink = 0
            profile.isFile =0
            profile.isCarrer = 0 
            profile.isReview = 0
            profile.save()
            auth.login(request, user)
            return redirect('/')
    else :
        return render(request, 'signup.html')

def signup_n(request):
    if request.method == "POST": 
        obj = json.loads(request.body)  
        user_name= obj['name']
        user_id = obj['id']
        # user_phone = obj['phone']s
        if User.objects.filter(username=user_id).exists():
            user = authenticate(request, username=user_id, password='0000')
            auth.login(request,user)
            return render(request, 'signup.html')   
        else:
            user = User.objects.create_user(username=user_id, password='0000')
            profile = Profile()
            profile.user_id = user
            profile.name = user_name
            mbti = Mbti.objects.get(id=1)
            profile.mbti_id =  mbti# 추후 수정 필요
            mbti.mbti_cnt = mbti.mbti_cnt + 1
            mbti.save()
            profile.email ='user_email' # 추후 수정 필요
            profile.phone =  "010-1234-5678"
            profile.birthday = "2021-07-10" # 추후 수정 필요
            profile.region1_id = Region1.objects.get(id=1) # 추후 수정 필요
            profile.region2_id = Region2.objects.get(id=1) # 추후 수정 필요
            profile.openPhone = 0
            profile.openEmail = 0 
            profile.term_id =  Term.objects.get(id=1) # 추후 수정 필요
            profile.field1_id = Field1.objects.get(id=1) # 추후 수정 필요
            profile.field2 = "Field2" # 추후 수정 필요
            profile.state = 1 
            profile.job_id =  Job.objects.get(id=1) # 추후 수정 필요
            profile.isLink = 0
            profile.isFile =0
            profile.isCarrer = 0 
            profile.isReview = 0
            profile.save()
            auth.login(request, user)
            return redirect('/')
    else :
        return render(request, 'signup.html')

        
# 로그인 함수
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            remember_session = request.POST.get('remember_session', False)
            if remember_session:
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
            return redirect('/')
        else:
            return render(request, 'login.html',{'error':"사용자 이름 혹은 패스워드가 일치하지 않습니다."})
    else:
        return render(request, 'login.html')

# # 회원가입 함수
# def signup(request):
#     if request.method == "POST":   
#         username = request.POST['username']
#         password = request.POST['password']
#         passwordCheck = request.POST['passwordCheck']
#         name = request.POST['name']
#         phone = request.POST['phone']
#         if not (username and password and passwordCheck and name and phone) :
#             return render(request, 'signup_back.html', {'error':"모든 값을 입력해주세요."})
#         elif User.objects.filter(username=username).exists():
#             return render(request, 'signup_back.html', {'error':"이미 존재하는 아이디입니다."})
#         elif Profile.objects.filter(phone = phone).exists():
#             return render(request, "signup_back.html", {'error': '이미 등록된 연락처입니다.'})
#         elif password != passwordCheck :
#             return render(request, "signup_back.html", {'error': '비밀번호가 일치하지 않습니다.'})     
#         else:
#             user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
#             profile = Profile()
#             profile.user_id = user
#             profile.name = name
#             mbti = Mbti.objects.get(id=1)
#             profile.mbti_id =  mbti# 추후 수정 필요
#             mbti.mbti_cnt = mbti.mbti_cnt + 1
#             mbti.save()
#             profile.email = "email" # 추후 수정 필요
#             profile.phone =  phone
#             profile.birthday = "2021-07-10" # 추후 수정 필요
#             profile.region1_id = Region1.objects.get(id=1) # 추후 수정 필요
#             profile.region2_id = Region2.objects.get(id=1) # 추후 수정 필요
#             profile.openPhone = 0
#             profile.openEmail = 0 
#             profile.term_id =  Term.objects.get(id=1) # 추후 수정 필요
#             profile.field1_id = Field1.objects.get(id=1) # 추후 수정 필요
#             profile.field2 = "Field2" # 추후 수정 필요
#             profile.state = 1 
#             profile.job_id =  Job.objects.get(id=1) # 추후 수정 필요
#             profile.isLink = 0
#             profile.isFile =0
#             profile.isCarrer = 0 
#             profile.photo = "Photo" # 추후 수정 필요
#             profile.isReview = 0
#             profile.save()
#             auth.login(request, user)
#             return redirect('/')
#     else :
#         return render(request, 'signup_back.html')
        
# # 로그인 함수
# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             remember_session = request.POST.get('remember_session', False)
#             if remember_session:
#                 settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
#             return redirect('/')
#         else:
#             return render(request, 'login_back.html',{'error':"사용자 이름 혹은 패스워드가 일치하지 않습니다."})
#     else:
#         return render(request, 'login_back.html')

# 로그아웃 함수
def logout_back(request):
    auth.logout(request)
    return redirect('/')

# 팀원 찾기 > 검색 함수
# def searchMember(request):
#     post = Profile.objects.all().order_by('id')
#     profiles_reg = Profile.objects.all().order_by('id')[:4]
#     field1 = Field1.objects.all() # 대분야 (ex IT)
#     mbti = Mbti.objects.all()
#     region2 = Region2.objects.all() # ~시 (서울만 ~구)
#     term = Term.objects.all()
#     job = Job.objects.all()
#     search = request.POST.get('examine')
#     if search:
#         post = post.filter(
#             Q(name__icontains = search)
#             #Q(mbti_id__icontains = search)|
#             #Q(field1_id__icontains = search)|
#             #Q(type__icontains = search)|
#             #Q(job_id__icontains = search)|
#             #Q(region1_id__icontains = search)|
#         )
#         return render(request,'member_search.html',{'profiles':post, "field1s":field1, "mbtis" : mbti, 
#                                                     "region2s": region2, "terms": term, "jobs": job, "profiles_reg":profiles_reg})  

# 마이페이지 프로필 함수
# def mypage_profile(request):
#     user = request.user
#     profile = Profile.objects.get(user_id = user)
#     user_links = User_link.objects.filter(user_id = user)
#     user_files = User_file.objects.filter(user_id = user)
#     user_reviews = User_review.objects.filter(to_user_id = user)
#     user_carrers = User_carrer.objects.filter(user_id = user)
#     return render(request, "mypage_profile_back.html", {"profile":profile, "user_links": user_links, "user_files": user_files , 
#                 "user_reviews": user_reviews, "user_carrers":user_carrers})

# 팀원 찾기 > 검색 함수
def searchMember(request):
    obj = json.loads(request.body)
    value = obj['value']
    if value:
        profiles = Profile.objects.filter(Q(name__icontains = value)| Q(region1_id__region1__icontains = value) | Q(region2_id__region2__icontains = value)
                                        | Q(job_id__job__icontains = value) | Q(mbti_id__mbti__icontains = value)| Q(pr__icontains = value))
        return render(request,'member_list_form.html',{'profiles':profiles})
    else:
        return render(request, 'member_list_form.html')

# 팀원 찾기 > 세부 필터링 함수
def filterMember(request):
    obj = json.loads(request.body)
    current_page = int(obj['page'])
    start_page = (current_page-1)*18
    txt = obj['txt']
    if txt=="":
        profile = Profile.objects.all()
    else:
        profile = Profile.objects.filter(Q(name__icontains = txt)| Q(region1_id__region1__icontains = txt) | Q(region2_id__region2__icontains = txt)
                                        | Q(job_id__job__icontains = txt) | Q(mbti_id__mbti__icontains = txt)| Q(pr__icontains = txt))
    field1 = obj['field1']
    mbti = obj['mbti']
    region = obj['region']
    term = obj['term']
    state = obj['state']
    job = obj['job']
    if field1[0]=='all':field1=list(Field1.objects.values_list('id', flat=True))
    if mbti[0]=='all':mbti=list(Mbti.objects.values_list('id', flat=True))
    if region[0]=='all':region=list(Region2.objects.values_list('id', flat=True))
    if term[0]=='all':term=list(Term.objects.values_list('id', flat=True))
    if state[0]=='all':state=[0, 1, 2]
    if job[0]=='all':job=list(Job.objects.values_list('id', flat=True))
    profiles = profile.filter(field1_id__id__in=field1,mbti_id__id__in=mbti,region2_id__id__in=region,
                                    term_id__id__in=term, state__in=state, job_id__id__in=job).order_by('-id')
    page_len = len(profiles)//18
    if len(profiles)%18 != 0:
        page_len+=1
    page = list(range(1, page_len+1))
    profiles = profiles[start_page:start_page+18]
    return render(request, "member_list_form.html", {'profiles':profiles, "page": page, "current_page":current_page})

# #마이페이지 프로필 수정 함수
# def mypage_modify_profile_edit(request):
#     user = request.user
#     profile = Profile.objects.get(user_id = user)
#     field1 = Field1.objects.all()
#     mbtis = Mbti.objects.all()
#     job = Job.objects.all()
#     region1 =Region1.objects.all()
#     region2 =Region2.objects.all()
#     term =Term.objects.all()
#     user_links = User_link.objects.filter(user_id = user)
#     user_files = User_file.objects.filter(user_id = user)
#     user_carrers = User_carrer.objects.filter(user_id = user)
#     return render(request, "mypage_modify_profile_back_sunneng.html", {"term":term,"region2":region2,"region1":region1,"mbtis":mbtis,"job":job,"field1":field1,"profile":profile, "user_links": user_links, "user_files": user_files ,  "user_carrers":user_carrers})

# #마이페이지 프로필 update 함수
# def mypage_modify_profile_update(request):
#     user = request.user
#     name = request.POST.get('name')
#     job = Job.objects.get(id=request.POST.get('job_id'))
#     birthday = request.POST.get('birthday')
#     region1 = Region1.objects.get(id=request.POST.get('region1_id'))
#     region2 = Region2.objects.get(id=request.POST.get('region2_id'))
#     state = request.POST.get('state')
#     field1 = Field1.objects.get(id=request.POST.get('field1_id'))
#     field2 = request.POST.get('field2')
#     term = Term.objects.get(id=request.POST.get('term_id'))
#     mbti = Mbti.objects.get(id=request.POST.get('mbti_id'))
#     mbti_detail = request.POST.get('mbti_detail')
#     pr = request.POST.get('pr')
#     profile = Profile.objects.get(user_id = user)
#     save_mbti_id = profile.mbti_id.id
#     save_mbti = Mbti.objects.get(id=save_mbti_id)
#     save_mbti.mbti_cnt = save_mbti.mbti_cnt -1
#     save_mbti.save()
#     profile.name = name
#     profile.job_id = job
#     profile.birthday = birthday
#     profile.region1_id = region1
#     profile.region2_id = region2
#     profile.state = state
#     profile.field1_id = field1
#     profile.field2 = field2
#     profile.term_id = term  
#     profile.mbti_id =mbti
#     mbti.mbti_cnt = mbti.mbti_cnt + 1
#     mbti.save()
#     profile.mbti_detail = mbti_detail
#     profile.pr = pr
#     # user_links = User_link.objects.filter(user_id = user) # 링크 여러개 수정할 수 있도록
#     # user_links.link = request.POST.get('link')
#     # if(request.FILES.getlist('user_files')): 
#     #         profile.isfile = 1
#     # user_carrers = User_carrer.objects.filter(user_id = user) # 커리어 여러개 수정할 수 있도록
#     # user_carrers.start_date = request.POST.get('start_date')
#     # user_carrers.end_date = request.POST.get('end_date')
#     # user_carrers.content = request.POST.get('content')
#     profile.submit = 1
#     profile.save()
#     # for files in request.FILES.getlist('user_files'): # 파일 여러개 수정할 수 있도록
#     #     user_files = User_file()
#     #     user_files.profile_id = profile
#     #     user_files.file = files
#     #     user_files.save()
#     #     profile.isFile = 1
#     #     profile.save() 
#     return redirect('/member/mypage')

# 마이페이지 함수
def mypage(request):
    return render(request, "mypage.html")

# 마이페이지 프로필 메뉴 함수 
def mypage_profile(request):
    user = request.user
    profile = Profile.objects.get(user_id = user)
    user_links = User_link.objects.filter(user_id = user)
    user_files = User_file.objects.filter(user_id = user)
    user_reviews = User_review.objects.filter(to_user_id = user)
    user_carrers = User_carrer.objects.filter(user_id = user)
    user_review = User_review.objects.filter(to_user_id = profile.user_id).order_by('-id')
    user_review_avg = User_review.objects.filter(to_user_id = profile.user_id).aggregate(Avg('total'))
    user_review_cnt = len(User_review.objects.filter(to_user_id = profile.user_id))
    user_review_1 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 1))
    user_review_2 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 2))
    user_review_3 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 3))
    user_review_4 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 4))
    user_review_5 = len(User_review.objects.filter(to_user_id = profile.user_id, total = 5))
    user_review_all = [user_review_1, user_review_2, user_review_3, user_review_4, user_review_5]
    return render(request, "mypage_profile.html", {"profile":profile, "user_links": user_links, "user_files": user_files , 
                "user_reviews": user_reviews, "user_carrers":user_carrers, "user_review": user_review, "user_review_all": user_review_all,
                "user_review_avg": user_review_avg, "user_review_cnt": user_review_cnt})

# 마이페이지 프로젝트 함수
def mypage_project(request):
    projects = Project.objects.filter(user_id=request.user).order_by('-id')
    member_list = {}
    for project in projects:
        member_list[project.id] = Member.objects.filter(project_id = project)
    return render(request, "mypage_project.html", {'projects':projects, "member_list": member_list.items()})

# 마이페이지 프로필 수정 페이지 함수
def mypage_modify_profile(request):
    user = request.user
    profile = Profile.objects.get(user_id = user)
    field1 = Field1.objects.all()
    mbtis = Mbti.objects.all()
    job = Job.objects.all()
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
    term =Term.objects.all()
    user_links = User_link.objects.filter(user_id = user)
    user_files = User_file.objects.filter(user_id = user)
    user_carrers = User_carrer.objects.filter(user_id = user)
    return render(request, "mypage_modify_profile.html", {"term":term,"region1s": region1, "region1_list": region1_list.items(), "region_list":region_list,"mbtis":mbtis,"job":job,"field1":field1,"profile":profile, "user_links": user_links, "user_files": user_files ,  "user_carrers":user_carrers})
# 마이페이지 프로필 수정 페이지 함수 - 대표사진 업로드 
def upload_profile_photo(request, profile_id):
    profile = Profile.objects.get(id = profile_id)
    file = request.FILES.get('file')
    profile.photo = file
    profile.save()
    return JsonResponse({"suc": 'success'})


def modify_profile(request):
    obj = json.loads(request.body)
    profile_id = obj['profile_id']
    job_id = obj['job_id']
    job = Job.objects.get(id = job_id)
    region1_id = obj['region1_id']
    region1 = Region1.objects.get(id=region1_id)
    region2_id = obj['region2_id']
    region2 = Region2.objects.get(id=region2_id)
    state = obj['state']
    field1_id = obj['field1_id']
    field1 = Field1.objects.get(id=field1_id)
    field2 = obj['field2']
    term_id = obj['term']
    term = Term.objects.get(id=term_id)
    mbti_id = obj['mbti']
    mbti = Mbti.objects.get(id=mbti_id)
    mbti.mbti_cnt = mbti.mbti_cnt+1
    mbti.save()
    mbti_detail = obj['mbti_detail']
    phone = obj['phone']
    email = obj['email']
    pr = obj['pr']
    profile = Profile.objects.get(id = profile_id)
    profile.job_id = job
    profile.region1_id = region1
    profile.region2_id = region2
    profile.state = state
    profile.field1_id = field1
    profile.field2 = field2
    profile.term_id = term
    m_save = profile.mbti_id
    m_save.mbti_cnt = m_save.mbti_cnt - 1
    m_save.save()
    profile.mbti_id = mbti
    profile.mbti_detail = mbti_detail
    profile.phone = phone
    profile.email = email
    profile.pr = pr
    profile.submit = 1
    profile.save()
    res = {
        'suc':"success",
    }
    return JsonResponse(res)
# 마이페이지 좋아요 페이지 함수
def mypage_like(request):
    user = request.user
    project_like = Like.objects.filter(type=0, from_user_id = user).values('project_id')
    project_like = list(project_like)
    project_like_list = [d['project_id'] for d in project_like]
    projects = Project.objects.filter(id__in = project_like_list).order_by('-id')
    member_like = Like.objects.filter(type = 1,  from_user_id = user).values('to_user_id')
    member_like = list(member_like)
    member_like_list = [d['to_user_id'] for d in member_like]
    like_users = User.objects.filter(id__in=member_like_list)
    profiles = Profile.objects.filter(user_id__in=like_users)
    projects_list = Project.objects.filter(id__in = project_like_list).order_by('-id')
    profiles_list = Profile.objects.filter(user_id__in=like_users)
    page = request.GET.get('page')
    paginator = Paginator(projects_list, 5)
    paginator = Paginator(profiles_list, 5)
    posts = paginator.get_page(page)
    return render(request, "mypage_like.html", {'projects':projects, "profiles":profiles,"posts":posts})

# 마이페이지 스크랩 페이지 함수
def mypage_scrap(request):
    user = request.user
    project_scrap = Scrap.objects.filter(type=0, from_user_id = user).values('project_id')
    project_scrap = list(project_scrap)
    project_scrap_list = [d['project_id'] for d in project_scrap]
    projects = Project.objects.filter(id__in = project_scrap_list).order_by('-id')
    member_scrap = Scrap.objects.filter(type = 1,  from_user_id = user).values('to_user_id')
    member_scrap = list(member_scrap)
    member_scrap_list = [d['to_user_id'] for d in member_scrap]
    scrap_users = User.objects.filter(id__in=member_scrap_list)
    profiles = Profile.objects.filter(user_id__in=scrap_users)
    return render(request, "mypage_scrap.html", {'projects':projects, "profiles":profiles})

#좋아요 만들어지는 함수 create
def likes(request):
    obj = json.loads(request.body) #받아온 data를 풀어주기 
    like=Like()
    to_user_id = User.objects.get(id=obj['value']) # Profile.objects.get(id=obj['value']) #profile.user_id.id
    like.type = int(1)
    like.to_user_id = to_user_id 
    # 오류가 뜨는데 어떻게 고쳐야 될지 모르겠다..
    # #ValueError: Cannot assign "<Profile: 조자운>": "Like.to_user_id" must be a "User" instance.
    like.from_user_id = request.user
    like.save()
    #알람기능 추가
    profile = Profile.objects.get(user_id=request.user)
    if like.to_user_id != request.user:
        alarm=Alarm()
        alarm.type = int(0)
        alarm.user_id = to_user_id
        alarm.like_id = like    
        alarm.member_url = '/member/member_detail/' + str(profile.id)
        alarm.save()
    else:
        return render(request,'member_search.html')
    return render(request,'member_search.html')

#좋아요 취소 함수
def likecancels(request):
    #profile.user_id.id
    obj = json.loads(request.body) #받아온 data를 풀어주기  project_id를 가져올것
    to_user_id = User.objects.get(id=obj['value'])
    Like.objects.get(to_user_id = to_user_id, from_user_id = request.user).delete() #like모델에 저장된 project_id랑 좋아요를 다시 클릭해서 얻어온 프로파일.user_id.id
    return render(request,'member_search.html')

# 팀원 찾기 최신순 정렬 함수
def latestMember(request):
    obj = json.loads(request.body)
    field1 = obj['field1']
    mbti = obj['mbti']
    region = obj['region']
    term = obj['term']
    state = obj['state']
    job = obj['job']
    if field1[0]=='all':field1=list(Field1.objects.values_list('id', flat=True))
    if mbti[0]=='all':mbti=list(Mbti.objects.values_list('id', flat=True))
    if region[0]=='all':region=list(Region2.objects.values_list('id', flat=True))
    if term[0]=='all':term=list(Term.objects.values_list('id', flat=True))
    if state[0]=='all':state=[0, 1, 2]
    if job[0]=='all':job=list(Job.objects.values_list('id', flat=True))
    profiles = Profile.objects.filter(field1_id__id__in=field1,mbti_id__id__in=mbti,region2_id__id__in=region,
                                    term_id__id__in=term, state__in=state, job_id__id__in=job).order_by('-id')
    return render(request, "member_list_form.html", {'profiles':profiles})

# 팀원 찾기 최신순 정렬 함수
def popularMember(request):
    obj = json.loads(request.body)
    field1 = obj['field1']
    mbti = obj['mbti']
    region = obj['region']
    term = obj['term']
    state = obj['state']
    job = obj['job']
    if field1[0]=='all':field1=list(Field1.objects.values_list('id', flat=True))
    if mbti[0]=='all':mbti=list(Mbti.objects.values_list('id', flat=True))
    if region[0]=='all':region=list(Region2.objects.values_list('id', flat=True))
    if term[0]=='all':term=list(Term.objects.values_list('id', flat=True))
    if state[0]=='all':state=[0, 1, 2]
    if job[0]=='all':job=list(Job.objects.values_list('id', flat=True))
    profiles = Profile.objects.filter(field1_id__id__in=field1,mbti_id__id__in=mbti,region2_id__id__in=region,
                                    term_id__id__in=term, state__in=state, job_id__id__in=job).values('user_id').order_by('-id')
    user = User.objects.filter(id__in = profiles)
    like = Like.objects.filter(type = 1, to_user_id__in = user).values('to_user_id').annotate(cnt = Count('to_user_id')).order_by('-cnt')
    like_list = list(like)
    like_id = [d['to_user_id'] for d in like_list]
    profiles = []
    for i in like_id:
        user = User.objects.get(id = i)
        p = Profile.objects.get(user_id = user)
        profiles.append(p)
    not_like_profiles = Profile.objects.filter(field1_id__id__in=field1,mbti_id__id__in=mbti,region2_id__id__in=region,
                                    term_id__id__in=term, state__in=state, job_id__id__in=job).exclude(user_id__in = like_id).order_by('-id')
    return render(request, "member_list_form.html", {'profiles':profiles, "not_like_profiles":not_like_profiles})

# 알람 페이지 html 렌더링
def alarm_detail(request):
    user = request.user
    profiles = Profile.objects.all()
    alarms = Alarm.objects.filter(user_id=user).order_by('-send_date')
    print(len(alarms))
    for alarm in alarms:
        if alarm.check == 0:
            alarm.check = int(1)
            alarm.check_date = timezone.now()
            alarm.save()
    page = request.GET.get('page')
    paginator = Paginator(alarms, 25)
    alarms = paginator.get_page(page)
    return render(request, "alarm_detail.html", {'alarms':alarms, 'profiles':profiles})

# 메시지 페이지 로딩 함수
def message(request):
    to_members = Message.objects.filter(from_user_id = request.user).values('to_user_id').distinct()
    from_members = Message.objects.filter(to_user_id = request.user).values('from_user_id').distinct()
    member_list = {}
    for mem in to_members:
        user = User.objects.get(id = mem['to_user_id'])
        name = Profile.objects.get(user_id = user)
        member_list[name.name] = user.id
    for mem in from_members:
        user = User.objects.get(id = mem['from_user_id'])
        name = Profile.objects.get(user_id = user)
        member_list[name.name] = user.id
    # for mem in member_list:
    #     print(member_list[mem])
    for mem in member_list:
        user = User.objects.get(id=member_list[mem])
        msg = Message.objects.filter(from_user_id=user, to_user_id=request.user).last()
        if(msg is not None):
            member_list[mem] = [member_list[mem], msg.state]
        else: member_list[mem] = [member_list[mem], 1]
    try:
        pay = Message_payment.objects.get(user_id = request.user, use = 1, end_date__gte = datetime.datetime.now())
    except Message_payment.DoesNotExist:
        pay = None
    return render(request, "message.html", {'member_list':member_list.items(), "select_member": 0, "pay": pay})

def message_payment(request):
    return render(request, 'message_payment.html')

def save_message_payment(request, type):
    current = datetime.datetime.now()
    payment = Message_payment()
    payment.user_id = request.user
    if type == 1:
        payment.end_date = current + datetime.timedelta(days=1)
    elif type == 2:
        payment.end_date = current + datetime.timedelta(days=7)
    elif type == 3:
        payment.end_date = current + datetime.timedelta(days=30)
    else:
        payment.end_date = current + datetime.timedelta(days=365)
    payment.pay_type = type
    payment.save()
    return redirect('https://developers.kakao.com/demo/pay/index')

def load_message(request):
    obj = json.loads(request.body)
    user_id = obj['user_id']
    me = request.user
    message_list = Message.objects.filter(Q(from_user_id = me, to_user_id = user_id) | Q(from_user_id = user_id, to_user_id = me)).exclude(content = "").order_by('send_date')
    Message.objects.filter(from_user_id = user_id, to_user_id = me, state = 0).update(state = 1)
    # print(message_list)
    return render(request, 'load_message.html', {"message_list":message_list})

def send_message(request):
    obj = json.loads(request.body)
    to_user_id = obj['to_user_id']
    to_user = User.objects.get(id = to_user_id)
    content = obj['content']
    Message.objects.create(to_user_id = to_user, from_user_id = request.user, content = content)
    res = {
        'to_user_id':to_user_id,
        'content':content,
    }
    return JsonResponse(res)

# 디테일 페이지 - 메시지
def message_room(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    to_user = profile.user_id
    from_user = request.user
    msg = Message.objects.filter(Q(from_user_id = to_user, to_user_id = from_user) | Q(from_user_id = from_user, to_user_id = to_user))
    if not msg:
        Message.objects.create(to_user_id = to_user, from_user_id = from_user, content = "")
    to_members = Message.objects.filter(from_user_id = request.user).values('to_user_id').distinct()
    from_members = Message.objects.filter(to_user_id = request.user).values('from_user_id').distinct()
    member_list = {}
    for mem in to_members:
        user = User.objects.get(id = mem['to_user_id'])
        name = Profile.objects.get(user_id = user)
        member_list[name.name] = user.id
    for mem in from_members:
        user = User.objects.get(id = mem['from_user_id'])
        name = Profile.objects.get(user_id = user)
        member_list[name.name] = user.id
    for mem in member_list:
        user = User.objects.get(id=member_list[mem])
        msg = Message.objects.filter(from_user_id=user, to_user_id=request.user).last()
        if(msg is not None):
            member_list[mem] = [member_list[mem], msg.state]
        else: member_list[mem] = [member_list[mem], 1]
    try:
        pay = Message_payment.objects.get(user_id = request.user, use = 1, end_date__gte = datetime.datetime.now())
    except Message_payment.DoesNotExist:
        pay = None
    return render(request, "message.html", {'member_list':member_list.items(), "select_member": profile, "pay": pay})

#스크랩 함수
def scraps(request):
    obj = json.loads(request.body)
    scrap=Scrap()
    to_user_id = User.objects.get(id=obj['value'])
    scrap.type = int(1)
    scrap.from_user_id = request.user
    scrap.to_user_id = to_user_id 
    scrap.save()
    #알람기능 추가
    profile = Profile.objects.get(user_id=request.user)
    if scrap.to_user_id != request.user:
        alarm=Alarm()
        alarm.type = int(2)
        alarm.user_id = to_user_id
        alarm.scrap_id = scrap
        alarm.member_url = '/member/member_detail/' + str(profile.id)
        alarm.save()
    else:
        return render(request,'member_search_back.html')
    return render(request,'member_search_back.html')

#스크랩 취소 함수
def scrapcancels(request):
    obj = json.loads(request.body)
    to_user_id = User.objects.get(id=obj['value'])
    Scrap.objects.get(to_user_id = to_user_id, from_user_id = request.user).delete()
    return render(request,'member_search_back.html')