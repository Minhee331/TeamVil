from django.shortcuts import render , redirect
from .models import *
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile


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
        if request.POST["password"] == request.POST["passwordCheck"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password"])
            name = request.POST["name"]      
            Phone = request.POST["Phone"]
            user.profile.name = name
            user.profile.mbti_id = "mbti_아이디"
            user.profile.email = "이메일"
            user.profile.phone = Phone
            user.profile.birthday = "생일"
            user.profile.region1_id = "대지역"
            user.profile.region2_id = "세부지역"
            user.profile.openPhone = "번호공개여부"
            user.profile.openEmail = "이메일공개여부"
            user.profile.term_id = "기간"
            user.profile.field1_id = "대분야"
            user.profile.field2 = "세부분야"
            user.profile.state = "참여상태"
            user.profile.job_id = "직업"
            user.profile.isLink = "링크"
            user.profile.isFile ="파일"
            user.profile.isCarrer = "직업공개"
            user.profile.register  = "등록시간"
            user.profile.photo ="사진"
            user.profile.isReview ="리뷰개수"
            user.profile.view_cnt ="조회수"
            user.save()
            auth.login(request, user)
            return redirect('/')
        elif Profile.objects.filter(Phone=request.POST['Phone']).exists():
                return render(request, "signup_back.html", {'error': '이미 등록된 연락처입니다.'})
        elif request.POST['password'] != request.POST['passwordCheck'] :
                return render(request, "signup_back.html", {'error': '비밀번호가 일치하지 않습니다.'})
        elif Profile.objects.filter(name=request.POST['username']).exists():
            return render(request, 'signup_back.html', {'error':"이미 존재하는 사용자입니다."})       
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
            return redirect('/')
        else:
            return render(request, 'login_back.html',{'error':"사용자 이름 혹은 패스워드가 일치하지 않습니다."})
    else:
        return render(request, 'login_back.html')
