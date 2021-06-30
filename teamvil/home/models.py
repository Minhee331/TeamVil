from django.db import models

# Create your models here.
class Field1(models.Model):
    field1 = models.CharField(max_length=20)

class Education(models.Model):
    education = models.CharField(max_length=10)

class Region1(models.Model):
    region1 = models.CharField(max_length=20)

class Region2(models.Model):
    region1_id = models.ForeignKey(Region1, on_delete = models.CASCADE, db_column="region1_id")
    region2 = models.CharField(max_length=20)
