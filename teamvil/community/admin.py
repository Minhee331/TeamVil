from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Com)
admin.site.register(Comment)
admin.site.register(Info)
admin.site.register(Info_link)
admin.site.register(Info_file)