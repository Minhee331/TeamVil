from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.PROTECT, db_column="user_id")
    use = models.IntegerField(default=0)
    isEnd = models.IntegerField(default=0)
    type = models.IntegerField()
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    field1_id = models.ForeignKey('home.Field1', on_delete = models.CASCADE, db_column="field1_id")
    field2 = models.CharField(max_length=20)
    region1_id = models.ForeignKey('home.Region1', on_delete = models.CASCADE, db_column="region1_id")
    region2_id = models.ForeignKey('home.Region2', on_delete = models.CASCADE, db_column="region2_id")
    mem_total = models.IntegerField()
    mem_now = models.IntegerField()
    mem_duty = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    state = models.IntegerField(default=1)
    school = models.CharField(max_length=45, null=True)
    content = models.TextField()
    isLink = models.IntegerField(default=0)
    isFile = models.IntegerField(default=0)
    education_id = models.ForeignKey('home.Education', on_delete = models.CASCADE, db_column="education_id", null=True)
    view_cnt = models.IntegerField(default=0)
    register = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Project_link(models.Model):
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE, db_column="project_id")
    link = models.CharField(max_length=45)
    def __str__(self):
        return self.link


class Project_file(models.Model):
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE, db_column="project_id")
    file = models.FileField()
    def __str__(self):
        return self.file.url

class Duty(models.Model):
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE, db_column="project_id")
    total = models.IntegerField()
    now = models.IntegerField(default=0)
    desc = models.TextField()
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.project_id.title + " " + self.name

class Member(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE, db_column="project_id")
    duty_id = models.ForeignKey(Duty, on_delete = models.CASCADE, db_column="duty_id")
    register_state = models.IntegerField(default=0) #null값 주거나 default 주거나 해야되는데 어케할까요?
    def __str__(self):
        return self.project_id.title + " " + self.duty_id.name

class Question(models.Model):
    project_id = models.ForeignKey('project.Project', on_delete = models.CASCADE, db_column="project_id")
    type = models.IntegerField() # 0: 객관식 1: 단답 2: 주관
    isRequired = models.IntegerField() # 0: 필수 아님 1 : 필수
    content = models.CharField(max_length=200)
    choice_cnt = models.IntegerField(null=True)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100, null=True)
    choice4 = models.CharField(max_length=100, null=True)
    choice5 = models.CharField(max_length=100, null=True)

class Apply_form(models.Model):
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE, db_column="project_id")
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id") # 프로젝트 생성한 유저 id
    q1_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q1_id", related_name="q1_id")
    q2_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q2_id", related_name="q2_id", null=True)
    q3_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q3_id", related_name="q3_id", null=True)
    q4_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q4_id", related_name="q4_id", null=True)
    q5_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q5_id", related_name="q5_id", null=True)
    q6_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q6_id", related_name="q6_id", null=True)
    q7_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q7_id", related_name="q7_id", null=True)
    q8_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q8_id", related_name="q8_id", null=True)
    q9_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q9_id", related_name="q9_id", null=True)
    q10_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="q10_id", related_name="q10_id", null=True)
    update_date = models.DateTimeField(default=timezone.now)
    write_date = models.DateTimeField(default=timezone.now)

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete = models.CASCADE, db_column="question_id")
    type = models.IntegerField() # 0: 객관식 1: 단답 2: 주관
    choice_answer = models.IntegerField(null=True)
    choice_text = models.CharField(max_length=100, null=True)
    short_answer = models.CharField(max_length=100, null=True)
    long_answer = models.TextField(null=True)

class Application(models.Model):
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE, db_column="project_id")
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id") # 지원한 user_id
    a1_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a1_id", related_name="a1_id")
    a2_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a2_id", related_name="a2_id", null=True)
    a3_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a3_id", related_name="a3_id", null=True)
    a4_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a4_id", related_name="a4_id", null=True)
    a5_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a5_id", related_name="a5_id", null=True)
    a6_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a6_id", related_name="a6_id", null=True)
    a7_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a7_id", related_name="a7_id", null=True)
    a8_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a8_id", related_name="a8_id", null=True)
    a9_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a9_id", related_name="a9_id", null=True)
    a10_id = models.ForeignKey(Answer, on_delete=models.CASCADE, db_column="a10_id", related_name="a10_id", null=True)
    write_date = models.DateTimeField(default=timezone.now)
    state = models.IntegerField() #(열람 1 , 미열람 0 | 디폴트 0)