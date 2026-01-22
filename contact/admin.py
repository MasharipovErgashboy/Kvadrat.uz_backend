from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'created_at')
    readonly_fields = ('first_name', 'last_name', 'user_type', 'phone', 'message', 'created_at')

from .models import ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')

    def has_add_permission(self, request):
        # Allow adding only if no instance exists
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)
