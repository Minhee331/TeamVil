from django.db import models
from django.contrib.auth.models import User
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
    def __str__(self):
        return self.project_id.title + " " + self.duty_id.name
