from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[2][1]['fields'] = ("phone",
                                       'is_active',
                                       'is_staff',
                                       'is_superuser',
                                       'special_user',
                                       'is_membership',
                                       'Employee',
                                       'employer',
                                       'groups',
                                       'user_permissions'
                                       )
UserAdmin.list_display += ('is_special_user',"is_membership_user",'phone')
UserAdmin.search_fields += ("phone",)
admin.site.register(User, UserAdmin)
