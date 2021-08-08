from django import template
import datetime
from account.models import *
from community.models import *
from home.models import *


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
def Name(profile): #community.user_id // reply.user_id
     user = User.objects.get(id=profile)
     profile = Profile.objects.get(user_id = user) 
     name =  profile.name
     return name

@register.simple_tag
def get_profile_id(profile): #community.user_id // reply.user_id
     user = User.objects.get(id=profile)
     profile = Profile.objects.get(user_id = user) 
     id =  profile.id
     return id

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
