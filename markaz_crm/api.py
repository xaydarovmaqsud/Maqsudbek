from rest_framework.routers import DefaultRouter

from account.api_views import UserViewset,RoleViewset,PermissionViewset,StudentViewSet,TeacherViewSet
from course.api_views import CourseViewset,GroupViewset
router=DefaultRouter()

router.register('account',UserViewset,basename='account')
router.register('roles',RoleViewset,basename='roles')
router.register('permissions',PermissionViewset,basename='permissions')
router.register('course',CourseViewset,basename='course')
router.register('groups',GroupViewset,basename='groups')
router.register('student',StudentViewSet,basename='student')
router.register('teacher',TeacherViewSet,basename='teacher')
