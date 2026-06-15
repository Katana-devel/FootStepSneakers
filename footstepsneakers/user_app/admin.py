from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import SneakerUser


@admin.register(SneakerUser)
class SneakerUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('bio',)}),
    )
