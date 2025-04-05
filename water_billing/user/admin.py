from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Users

class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = (
        'account_id', 'username', 'email', 'first_name', 
        'last_name', 'role', 'is_staff', 'is_active', 'date_joined'
    )
    list_display_links = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'account_id', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'first_name', 'last_name', 
                'account_id', 'role', 'password', 'is_staff', 'is_superuser'
            ),
        }),
    )
    ordering = ('date_joined',)
    search_fields = ('account_id', 'username', 'email', 'first_name', 'last_name')
    list_editable = ('account_id', 'role', 'is_staff')
admin.site.register(Users, CustomUserAdmin)
