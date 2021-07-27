from django import template
import datetime
from account.models import *


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

    # {$ Name comment.user_id.id $} 