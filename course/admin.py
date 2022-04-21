from django.contrib import admin

from group.models import Group, GroupStudent
from .models import Course,TeacherCourse

admin.site.register(Course)
admin.site.register(TeacherCourse)
admin.site.register(Group)
admin.site.register(GroupStudent)
