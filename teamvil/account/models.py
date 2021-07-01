from django.db import models
from django.contrib.auth.models import User
from home.models import Field1, Region1, Region2, Education

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
    term_type = models.CharField(max_length=10)
    def __str__(self):
        return self.term

class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    name = models.CharField(max_length=25)
    mbti_id = models.ForeignKey(Mbti, on_delete = models.CASCADE, db_column="mbti_id")
    mbti_detail = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
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
    register = models.DateTimeField()
    photo = models.CharField(max_length=100)
    isReview = models.IntegerField()
    view_cnt = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class User_link(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    link = models.CharField(max_length=45)
    def __str__(self):
        return self.link

class User_file(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    file = models.CharField(max_length=45)
    def __str__(self):
        return self.file

class User_carrer(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column="user_id")
    file = models.CharField(max_length=45)
    start_date = models.DateField()
    end_date = models.DateField()
    content = models.TextField()
    def __str__(self):
        return self.file
