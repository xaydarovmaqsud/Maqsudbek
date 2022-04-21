from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='groups')
    duration = models.IntegerField(default=0)
    start_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

class GroupStudent(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='group_student')
    group = models.ForeignKey('group.Group', on_delete=models.CASCADE, related_name='group_student')