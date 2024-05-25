from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'first_name',
        'last_name',
        'department'
        'email',
        'is_staff',
        'is_active',
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'department')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permission')
        }),
        ('Important data', {'fields': ('last_login', 'date_joined')}),
    )
