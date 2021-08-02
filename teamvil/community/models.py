from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Com(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    update_date = models.DateTimeField(auto_now=True)
    write_date = models.DateTimeField(auto_now_add= True)
    content = models.TextField()
    view_cnt = models.IntegerField(default=0)

class Comment(models.Model):
    parent = models.IntegerField() #댓글(0) - 대댓글(!0) , 대댓글 id의 번호를 가지고 온다. // c. comment_id = c.id // 부모댓글의 id 
    content = models.TextField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    com_id = models.ForeignKey(Com, on_delete = models.CASCADE, db_column="com_id")
    update_date = models.DateTimeField(auto_now=True)
    write_date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.content

class Info(models.Model):
    state = models.IntegerField(default=0) # 0 게시 요청, 1 게시, 2 반려
    host = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True)
    update_date = models.DateTimeField(default=timezone.now)
    write_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    content = models.TextField()
    isLink = models.IntegerField(default=0)
    isFile = models.IntegerField(default=0)
    view_cnt = models.IntegerField(default=0)

class Info_link(models.Model):
    info_id = models.ForeignKey(Info, on_delete = models.CASCADE, db_column="info_id")
    link = models.CharField(max_length=45)
    def __str__(self):
        return self.link


class Info_file(models.Model):
    info_id = models.ForeignKey(Info, on_delete = models.CASCADE, db_column="info_id")
    file = models.FileField()
    def __str__(self):
        return self.file

