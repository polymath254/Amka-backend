
from django.contrib import admin
from .models import FormType, FormSubmission

@admin.register(FormType)
class FormTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'form_type', 'full_name', 'email', 'region', 'is_approved', 'submitted_at'
    )
    list_filter = ('form_type', 'region', 'is_approved')
    search_fields = ('full_name', 'email', 'content', 'data')
    actions = ['approve_submissions', 'export_selected']

    def approve_submissions(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} submission(s) approved.")
    approve_submissions.short_description = "Approve selected submissions"

    def export_selected(self, request, queryset):
        # Placeholder for CSV/XLSX export logic
        self.message_user(request, "Export feature coming soon!")
    export_selected.short_description = "Export selected to CSV/XLSX"

