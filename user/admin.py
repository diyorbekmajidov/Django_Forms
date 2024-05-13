from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": ['password', 'email', 'username'],}),
        ("Content", {"fields": ['status'],}),
    ]

admin.site.register(CustomUser, CustomUserAdmin)
