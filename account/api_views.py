from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import mixins
from account.models import User, Role, Permission, UserRole, UserTag
from account.serializers import UserSerialiser,RoleSerialiser,PermissionSerialiser ,UserRoleSerialiser


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

class RoleViewset(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerialiser

class PermissionViewset(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerialiser

class UserRoleViewset(ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerialiser

class StudentViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = User.objects.filter(id__in=[i.user.id for i in UserTag.objects.filter(tag__name='Student')])
    serializer_class = UserSerialiser
    def get_queryset(self):
        return User.objects.filter(id__in=[i.user.id for i in UserTag.objects.filter(tag__name='Student')])

class TeacherViewSet(ModelViewSet):
    queryset = User.objects.filter(id__in=[i.user.id for i in UserTag.objects.filter(tag__name='Teacher')])
    serializer_class = UserSerialiser
