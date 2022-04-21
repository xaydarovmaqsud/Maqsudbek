from django.contrib import admin
from .models import User,UserRole,Role,Permission,RolePermission,Tag,UserTag

class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']
    list_display_links = ['name']
    search_fields = ['id','name','description']

admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(RolePermission)
admin.site.register(Tag,TagAdmin)
admin.site.register(UserTag)
