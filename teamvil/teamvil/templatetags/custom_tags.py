from django import template
import datetime



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


