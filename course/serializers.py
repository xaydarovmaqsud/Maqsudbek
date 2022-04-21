from rest_framework.serializers import ModelSerializer

from group.models import Group
from .models import Course


class CourseSerialiser(ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class GroupSerialiser(ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'