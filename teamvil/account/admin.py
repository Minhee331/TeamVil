from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Mbti)
admin.site.register(Job)
admin.site.register(Term)
admin.site.register(Profile)
admin.site.register(User_link)
admin.site.register(User_file)
admin.site.register(User_carrer)
admin.site.register(User_review)
admin.site.register(Message)

class ProfileAdmin(admin.StackedInline):
    model = Profile
    con_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileAdmin,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)