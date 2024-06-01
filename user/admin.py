from django.contrib import admin
from .models import CustomUser,SubscribedUsers


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')

class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Header', {'fields': ['username', 'password','image']}),
        ('Personal info', {'fields': ['email', 'status']}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser',]}),
        ('Important dates', {'fields': ['last_login',]}),
    ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SubscribedUsers, SubscribedUsersAdmin)
