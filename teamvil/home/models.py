from django.db import models
from django.contrib.auth.models import User
from community.models import Com, Info
from django.utils import timezone


# Create your models here.
class Field1(models.Model):
    field1 = models.CharField(max_length=20)
    def __str__(self):
        return self.field1

class Education(models.Model):
    education = models.CharField(max_length=10)
    def __str__(self):
        return self.education

class Region1(models.Model):
    region1 = models.CharField(max_length=20)
    def __str__(self):
        return self.region1

class Region2(models.Model):
    region1_id = models.ForeignKey(Region1, on_delete = models.CASCADE, db_column="region1_id")
    region2 = models.CharField(max_length=20)
    def __str__(self):
        return self.region1_id.region1 + " " + self.region2

class Like(models.Model):
    type = models.IntegerField()
    project_id = models.ForeignKey('project.Project', on_delete = models.CASCADE, db_column="project_id", null=True)
    com_id = models.ForeignKey(Com, on_delete = models.CASCADE, db_column="com_id", null=True)
    info_id = models.ForeignKey(Info, on_delete = models.CASCADE, db_column="info_id", null=True)
    from_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="from_user_id", related_name="like_from_user_id")
    to_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="to_user_id", related_name="like_to_user_id", null=True)

class Scrap(models.Model):
    type = models.IntegerField()
    project_id = models.ForeignKey('project.Project', on_delete = models.CASCADE, db_column="project_id", null=True)
    from_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="from_user_id", related_name="scrap_from_user_id")
    to_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="to_user_id", related_name="scrap_to_user_id", null=True)

class Noti(models.Model):
    to_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="to_user_id", related_name="noti_to_user_id", null=True)
    type = models.IntegerField()
    project_id = models.ForeignKey('project.Project', on_delete = models.CASCADE, db_column="project_id", null=True)
    message_id = models.ForeignKey('account.Message', on_delete = models.CASCADE, db_column="message_id", null=True)
    rec_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="rec_user_id", related_name="rec_to_user_id", null=True)
    content = models.CharField(max_length=300)
    send_date = models.DateTimeField(auto_now_add= True)
    url = models.CharField(max_length=100)

class Alarm(models.Model):
    type = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    member_id = models.ForeignKey('project.Member', on_delete = models.CASCADE, db_column="member_id", null=True)
    like_id = models.ForeignKey(Like, on_delete = models.CASCADE, db_column="like_id", null=True)
    scrap_id = models.ForeignKey(Scrap, on_delete = models.CASCADE, db_column="scrap_id", null=True)
    content = models.CharField(max_length=300)
    url = models.CharField(max_length=200)
    send_date = models.DateTimeField(default=timezone.now)
    check_date = models.DateTimeField(null=True)
    check = models.IntegerField(default=0)