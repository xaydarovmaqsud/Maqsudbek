from rest_framework.serializers import ModelSerializer
from account.models import User,Role,Permission,UserRole


class UserSerialiser(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class RoleSerialiser(ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'

class PermissionSerialiser(ModelSerializer):
    class Meta:
        model=Permission
        fields='__all__'

class UserRoleSerialiser(ModelSerializer):
    class Meta:
        model=UserRole
        fields='__all__'