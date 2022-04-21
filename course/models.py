from django.db import models
from account.models import User


class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    price=models.FloatField(default=0)

    def __str__(self):
        return self.name

class TeacherCourse(models.Model):
    user=models.ForeignKey('account.User',on_delete=models.CASCADE,related_name='teacher_course')
    course=models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='teacher_course')

    def __str__(self):
        return f'{self.user} -> {self.course}'


