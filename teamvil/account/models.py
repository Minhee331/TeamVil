from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from home.models import Field1, Region1, Region2, Education
from project.models import Project


# Create your models here.
class Mbti(models.Model):
    mbti = models.CharField(max_length=4)
    mbti_cnt = models.IntegerField(default=0)
    def __str__(self):
        return self.mbti

class Job(models.Model):
    job = models.CharField(max_length=20)
    def __str__(self):
        return self.job

class Term(models.Model):
    term = models.CharField(max_length=20)
    term_type = models.IntegerField()
    def __str__(self):
        return self.term

class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    name = models.CharField(max_length=25)
    mbti_id = models.ForeignKey(Mbti, on_delete = models.CASCADE, db_column="mbti_id")
    mbti_detail = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
    type = models.IntegerField(default=0) # 창업0, 공모전1, 프로젝트2 선호 프로젝트 타입
    region1_id = models.ForeignKey(Region1, on_delete = models.CASCADE, db_column="region1_id")
    region2_id = models.ForeignKey(Region2, on_delete = models.CASCADE, db_column="region2_id")
    openPhone = models.IntegerField()
    openEmail = models.IntegerField()
    term_id = models.ForeignKey(Term, on_delete = models.CASCADE, db_column="term_id")
    field1_id = models.ForeignKey(Field1, on_delete = models.CASCADE, db_column="field1_id")
    field2 = models.CharField(max_length=20)
    state = models.IntegerField()
    job_id = models.ForeignKey(Job, on_delete = models.CASCADE, db_column="job_id")
    education_id = models.ForeignKey(Education, on_delete = models.CASCADE, db_column="education_id", null=True)
    isLink = models.IntegerField()
    isFile = models.IntegerField()
    isCarrer = models.IntegerField()
    pr = models.TextField(null=True)
    register = models.DateTimeField(default=timezone.now)
    photo = models.FileField(null=True)
    isReview = models.IntegerField()
    view_cnt = models.IntegerField(default=0)
    submit = models.IntegerField(default=0)
    def __str__(self):
        return self.name

 


class User_link(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    link = models.CharField(max_length=45)
    def __str__(self):
        return self.link

class User_file(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    file = models.FileField()
    def __str__(self):
        return self.file.url

class User_carrer(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    start_date = models.DateField()
    end_date = models.DateField()
    content = models.TextField()
    def __str__(self):
        return self.content

class User_review(models.Model):
    from_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="from_user_id", related_name="review_from_user_id")
    to_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="to_user_id", related_name="review_to_user_id")
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE, db_column="project_id")
    content = models.TextField()
    total = models.IntegerField() # 0~5까지 1단위로
    def __str__(self):
        return str(self.total)

class Message(models.Model):
    from_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="from_user_id", related_name="message_from_user_id")
    to_user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="to_user_id", related_name="message_to_user_id")
    send_date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=1000)
    state = models.IntegerField(default=0) # 0 읽지 않음, 1 읽음

class Message_payment(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    pay_type = models.IntegerField() # (1: 1일, 2: 7일, 3: 1달, 4: 1년)
    use = models.IntegerField(default=1) # (0: 만료 1: 사용가능)
    
