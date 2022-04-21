from django.db import models

from account.models import User
from group.models import Group


class Room(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True,blank=True)

class Lesson(models.Model):
    group = models.ForeignKey('group.Group', on_delete=models.SET_NULL, null=True, related_name='lessons')
    room = models.ForeignKey('lesson.Room', on_delete=models.SET_NULL, null=True, related_name='lessons')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Attendance(models.Model):
    STATUSES = (
        ('came', 'Came'),
        ('uncame', 'Uncame'),
        ('reasone', 'Reasone'),
    )
    user = models.ForeignKey('account.User',on_delete=models.SET_NULL,null=True, related_name='attendences')
    lesson = models.ForeignKey('lesson.Lesson',on_delete=models.SET_NULL,null=True, related_name='attendences')
    status = models.CharField(max_length=20,default='uncame', choices=STATUSES)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} -> {self.lesson}'

class Task(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(null=True,blank=True)
    lesson = models.ForeignKey('lesson.Lesson', on_delete=models.SET_NULL, null=True, related_name='tasks')


class TaskFile(models.Model):
    task = models.ForeignKey('lesson.Task', on_delete=models.SET_NULL, null=True, related_name='task_file')
    file= models.ForeignKey('file_manager.FileManager', on_delete=models.CASCADE, related_name='task_file')


class Work(models.Model):
    user = models.ForeignKey('account.User',on_delete=models.SET_NULL,null=True, related_name='works')
    task = models.ForeignKey('lesson.Task', on_delete=models.SET_NULL, null=True, related_name='works')
    grade =  models.FloatField(null=True,blank=True)


class WorkFile(models.Model):
    work = models.ForeignKey('lesson.Work', on_delete=models.CASCADE, null=True, related_name='work_file')
    file= models.ForeignKey('file_manager.FileManager', on_delete=models.CASCADE, related_name='work_file')

class CommentLesson(models.Model):
    user = models.ForeignKey('account.User',on_delete=models.CASCADE, related_name='comments')
    lesson = models.ForeignKey('lesson.Lesson',on_delete=models.CASCADE, related_name='comments')
    description = models.TextField()
