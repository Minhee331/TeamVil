from django.shortcuts import render , redirect
from .models import *
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from django.conf import settings
from django.db.models import Q


# Create your views here.

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

def signup_back(request):
    if request.method == "POST":   
        # if not (profile.username and password and passwordCheck and name and phone) :
        #     return render(request, 'signup_back.html', {'error':"모든 값을 입력해주세요."})
        if Profile.objects.filter(phone=request.POST['phone']).exists():
            return render(request, "signup_back.html", {'error': '이미 등록된 연락처입니다.'})
        elif request.POST['password'] != request.POST['passwordCheck'] :
            return render(request, "signup_back.html", {'error': '비밀번호가 일치하지 않습니다.'})
        elif User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'signup_back.html', {'error':"이미 존재하는 아이디입니다."})               
        else:
            user = User.objects.create_user( username=request.POST["username"], password=request.POST["password"])
            profile = Profile()
            profile.user_id = user
            profile.name = request.POST['name']
            profile.mbti_id = Mbti.objects.get(id=1)
            profile.email = "email"
            profile.phone =  request.POST['phone']
            profile.birthday = "2021-07-10"
            profile.region1_id = Region1.objects.get(id=1)
            profile.region2_id = Region2.objects.get(id=1)
            profile.openPhone = 0
            profile.openEmail = 0
            profile.term_id =  Term.objects.get(id=1)
            profile.field1_id = Field1.objects.get(id=1)
            profile.field2 = "Field2"
            profile.state = 0
            profile.job_id =  Job.objects.get(id=1)
            profile.isLink = 0
            profile.isFile =0
            profile.isCarrer = 0
            profile.register  = "2021-07-10"
            profile.photo = "Photo"
            profile.isReview =0
            profile.view_cnt =0
            profile.save()
            auth.login(request, user)
            return redirect('/')
            
    else :
        return render(request, 'signup_back.html')


            # profile = Profile.objects.create(user=user, email=email, name=name, gender=gender, phone=phone, age=age,
            # color=color, purpose=purpose, introduce=introduce, school=school, major=major, region=region, state=state, photo=photo)
        

def login_back(request):
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

def logout_back(request):
    auth.logout(request)
    return redirect('/')

def search(request):
    post = Profile.objects.all().order_by('id')
    profiles_reg = Profile.objects.all().order_by('id')[:4]
    field1 = Field1.objects.all() # 대분야 (ex IT)
    mbti = Mbti.objects.all()
    region2 = Region2.objects.all() # ~시 (서울만 ~구)
    term = Term.objects.all()
    job = Job.objects.all()
    search = request.POST.get('examine')
    if search:
        post = post.filter(
            Q(name__icontains = search)
            #Q(mbti_id__icontains = search)|
            #Q(field1_id__icontains = search)|
            #Q(type__icontains = search)|
            #Q(job_id__icontains = search)|
            #Q(region1_id__icontains = search)|
        )
        return render(request,'member_search.html',{'profiles':post, "field1s":field1, "mbtis" : mbti, 
                                                    "region2s": region2, "terms": term, "jobs": job, "profiles_reg":profiles_reg})   
 