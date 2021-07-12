from django.db import models


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
