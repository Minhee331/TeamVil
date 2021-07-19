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

def member_search(request):
    profiles = Profile.objects.all()
    profiles_reg = Profile.objects.all().order_by('id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "member_search.html", {'profiles':profiles, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "profiles_reg":profiles_reg})


def member_search_back(request):
    profiles = Profile.objects.all()
    profiles_reg = Profile.objects.all().order_by('id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    return render(request, "member_search_back.html", {'profiles':profiles, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "profiles_reg":profiles_reg})


def member_search_back_cloud(request):
    profiles = Profile.objects.all()
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
    return render(request, "member_detail.html", {"profile":profile, "carrers":carrers,
                "user_links": user_links, "user_files": user_files})

def member_detail_back(request, profile_id):
    profile = Profile.objects.get(id = profile_id)
    carrers = User_carrer.objects.filter(user_id = profile.user_id)
    user_links = User_link.objects.filter(user_id = profile.user_id)
    user_files = User_file.objects.filter(user_id = profile.user_id)
    return render(request, "member_detail_back.html", {"profile":profile, "carrers":carrers,
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
            return render(request, 'signup_back.html', {'error':"모든 값을 입력해주세요."})
        elif User.objects.filter(username=username).exists():
            return render(request, 'signup_back.html', {'error':"이미 존재하는 아이디입니다."})
        elif Profile.objects.filter(phone = phone).exists():
            return render(request, "signup_back.html", {'error': '이미 등록된 연락처입니다.'})
        elif password != passwordCheck :
            return render(request, "signup_back.html", {'error': '비밀번호가 일치하지 않습니다.'})     
        else:
            user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
            profile = Profile()
            profile.user_id = user
            profile.name = name
            profile.mbti_id = Mbti.objects.get(id=1) # 추후 수정 필요
            profile.email = "email" # 추후 수정 필요
            profile.phone =  phone
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
            profile.photo = "Photo" # 추후 수정 필요
            profile.isReview = 0
            profile.save()
            auth.login(request, user)
            return redirect('/')
    else :
        return render(request, 'signup_back.html')
        
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
            return render(request, 'login_back.html',{'error':"사용자 이름 혹은 패스워드가 일치하지 않습니다."})
    else:
        return render(request, 'login_back.html')

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
                                    term_id__id__in=term, state__in=state, job_id__id__in=job).order_by('id')
    return render(request, "member_list_form.html", {'profiles':profiles})

#마이페이지 프로필 수정 함수
def mypage_modify_profile_edit(request):
    user = request.user
    profile = Profile.objects.get(user_id = user)
    field1 = Field1.objects.all()
    user_links = User_link.objects.filter(user_id = user)
    user_files = User_file.objects.filter(user_id = user)
    user_carrers = User_carrer.objects.filter(user_id = user)
    return render(request, "mypage_modify_profile_back_sunneng.html", {"field1":field1,"profile":profile, "user_links": user_links, "user_files": user_files , 
                    "user_carrers":user_carrers})
#마이페이지 프로필 update 함수
def mypage_modify_profile_update(request):
    user = request.user
    profile = Profile.objects.get(user_id = user)
    profile.name = request.POST.get('name')
    profile.job_id = request.POST.get('job_id_id')
    profile.birthday = request.POST.get('birthday')
    profile.region2_id = request.POST.get('region2_id')
    profile.state = request.POST.get('state')
    field1s = Field1.objects.all()
    profile.field1_id = request.POST.get('profile.field1.field1')
    profile.field2 = request.POST.get('field2')
    profile.term_id = request.POST.get('term_id.term_id')
    profile.mbti_id = request.POST.get('mbti_id.mbti_id')
    profile.mbti_detail = request.POST.get('mbti_detail')
    # profile.openPhone = request.POST.get('openPhone')
    # profile.openEmail = request.POST.get('openEmail')
    profile.pr = request.POST.get('pr')
    user_links = User_link.objects.filter(user_id = user)
    user_links.link = request.POST.get('link')
    user_files = User_file.objects.filter(user_id = user)
    user_files.file = request.POST.get('file')
    user_carrers = User_carrer.objects.filter(user_id = user)
    user_carrers.start_date = request.POST.get('start_date')
    user_carrers.end_date = request.POST.get('end_date')
    user_carrers.content = request.POST.get('content')
    profile.save()
    user_links.save()
    user_files.save()
    user_carrers.save()
    return render(request,'/member/mypage_modify_profile_back_sunneng/update' + str(profile.id),{"field1s":field1s})

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
    return render(request, "mypage_profile.html", {"profile":profile, "user_links": user_links, "user_files": user_files , 
                "user_reviews": user_reviews, "user_carrers":user_carrers})

# 마이페이지 프로젝트 함수
def mypage_project(request):
    user = request.user
    projects = Project.objects.filter(user_id=user)
    likes = Like.objects.filter(to_user_id =user)
    scraps = Scrap.objects.filter(to_user_id =user)
    return render(request, "mypage_project.html", {'projects':projects, "likes": likes,"scrpas": scraps})


#좋아요 카운팅 함수
def like(request):
    user = request.user
    profile = Profile.objects.get(user_id = user)
    like_to_user_id = Like.objects.get('to_user_id') #좋아요 당하는 사람
    like_from_user_id = Like.objects.get('from_user_id')  #나(좋아요를 누르는 사람) -> 이게 user가 되나?
