from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from group.models import Group
from .models import Course
from .serializers import CourseSerialiser,GroupSerialiser


class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerialiser

class GroupViewset(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerialiser