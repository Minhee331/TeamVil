from django import template
import datetime
from account.models import *
from community.models import *
from home.models import *
from project.models import *
from django.conf.urls.static import static
# from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()
@register.simple_tag
def getAge(birthday):
     now = int(datetime.datetime.today().year)
     birthday = int(birthday.strftime('%Y'))
     return now - birthday

@register.simple_tag
def DateFormat(birthday):
     birthday = birthday.strftime('%Y-%m-%d')
     return birthday

@register.simple_tag
def DateFormatDot(birthday):
     birthday = birthday.strftime('%Y.%m.%d')
     return birthday




@register.simple_tag
def Dday(end_date):
     #같은 달인경우
     f_now = int(datetime.datetime.today().month)
     f_end_date = int(end_date.strftime('%m'))
     now = int(datetime.datetime.today().day)
     end_date = int(end_date.strftime('%d'))
     if f_now == f_end_date :
          if now < end_date:
               return now - end_date
          else: 
               return "이미지난공고입니다"
     #다른 달인경우
     else :
          return now

@register.simple_tag
def Name(profile): #community.user_id // reply.user_id
     user = User.objects.get(id=profile)
     profile = Profile.objects.get(user_id = user) 
     name =  profile.name
     return name

@register.simple_tag
def get_profile_id(user_id): #community.user_id // reply.user_id
     user = User.objects.get(id=user_id)
     profile = Profile.objects.get(user_id = user) 
     id =  profile.id
     return id

@register.simple_tag
def get_profile_photo(user_id): #community.user_id // reply.user_id
     user = User.objects.get(id=user_id)
     profile = Profile.objects.get(user_id = user) 
     if profile.photo.url is not None:
          return profile.photo.url
     else:
          return ''

# {$ Name comment.user_id.id $} 
@register.simple_tag
def TimeFormat(write_date):
     write_date = write_date.strftime('%Y.%m.%d')
     return write_date
     
@register.simple_tag
def HourFormat(write_date):
     write_date = write_date.strftime('%H:%M')
     return write_date

@register.simple_tag
def active_like(type, id, u_id):
     # 0 프로젝트 1 멤버 2 자유 커뮤니티 3 정보
     active = ""
     user = User.objects.get(id = u_id)
     if(type == 0):
          project = Project.objects.get(id=id)
          cnt = Like.objects.filter(type=0, project_id=project, from_user_id = user).count()
          if cnt : active = "active"
     elif(type == 1):
          profile = Profile.objects.get(id=id)
          cnt = Like.objects.filter(type=1, to_user_id=profile.user_id, from_user_id = user).count()
          if cnt : active = "active"
     return  active

@register.simple_tag
def get_like_cnt(type, id):
     # 0 프로젝트 1 멤버 2 자유 커뮤니티 3 정보
     if(type == 0):
          project = Project.objects.get(id=id)
          cnt = Like.objects.filter(type=0, project_id=project).count()
     if(type == 1):
          profile = Profile.objects.get(id=id)
          cnt = Like.objects.filter(type=1, to_user_id=profile.user_id).count()
     return  cnt

@register.simple_tag
def get_scrap_cnt(type, id):
     # 0 프로젝트 1 멤버 2 자유 커뮤니티 3 정보
     if(type == 0):
          project = Project.objects.get(id=id)
          cnt = Scrap.objects.filter(type=0, project_id=project).count()
     if(type == 1):
          profile = Profile.objects.get(id=id)
          cnt = Scrap.objects.filter(type=1, to_user_id=profile.user_id).count()
     return  cnt

@register.simple_tag
def active_scrap(type, id, u_id):
     # 0 프로젝트 1 멤버 2 자유 커뮤니티 3 정보
     active = ""
     user = User.objects.get(id = u_id)
     if(type == 0):
          project = Project.objects.get(id=id)
          cnt = Scrap.objects.filter(type=0, project_id=project, from_user_id = user).count()
          if cnt : active = "active"
     elif(type == 1):
          profile = Profile.objects.get(id=id)
          cnt = Scrap.objects.filter(type=1, to_user_id=profile.user_id, from_user_id = user).count()
          if cnt : active = "active"
     return  active

@register.simple_tag
def get_mem_register(project_id):
     project = Project.objects.get(id = project_id)
     mem = Member.objects.filter(project_id = project, register_state = 1)
     return len(mem)

@register.simple_tag
def get_mem_name(mem_id):
     member = Member.objects.get(id = mem_id)
     profile = Profile.objects.get(user_id = member.user_id)
     return profile.name

@register.simple_tag
def get_mem_age(mem_id):
     member = Member.objects.get(id = mem_id)
     profile = Profile.objects.get(user_id = member.user_id)
     birthday = profile.birthday
     now = int(datetime.datetime.today().year)
     birthday = int(birthday.strftime('%Y'))
     return now - birthday

@register.simple_tag
def get_mem_region(mem_id):
     member = Member.objects.get(id = mem_id)
     profile = Profile.objects.get(user_id = member.user_id)
     return profile.region2_id

@register.simple_tag
def get_mem_phone(mem_id):
     member = Member.objects.get(id = mem_id)
     profile = Profile.objects.get(user_id = member.user_id)
     return profile.phone  

@register.simple_tag
def get_mem_email(mem_id):
     member = Member.objects.get(id = mem_id)
     profile = Profile.objects.get(user_id = member.user_id)
     return profile.email  

