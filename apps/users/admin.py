from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'email', 'is_approved', 'is_staff', 'is_active')
    list_filter = ('is_approved', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone')
    actions = ['approve_users', 'send_email_to_users']

    def approve_users(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} user(s) approved.")
    approve_users.short_description = "Approve selected users"

    def send_email_to_users(self, request, queryset):
        # Placeholder for sending emails in future
        self.message_user(request, "Email sending feature coming soon!")
    send_email_to_users.short_description = "Send email to selected users"

