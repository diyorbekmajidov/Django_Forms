from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Header', {'fields': ['username', 'password','image']}),
        ('Personal info', {'fields': ['email', 'status']}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser',]}),
        ('Important dates', {'fields': ['last_login',]}),
    ]

admin.site.register(CustomUser, CustomUserAdmin)
