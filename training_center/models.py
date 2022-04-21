from django.db import models
from account.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    price=models.FloatField(default=0)


class TeacherCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='course')
    course=models.ForeignKey(Course, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='group')
    duration=models.IntegerField(null=True,blank=True)
    start_time=models.DateTimeField(null=True,blank=True)
    default_lesson_time=models.TimeField

class GroupStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='grstudent')
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
