from django.contrib import admin
from .models import ContactSubmission, ContactInfo

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'created_at')
    readonly_fields = ('first_name', 'last_name', 'user_type', 'phone', 'message', 'created_at')
    list_filter = ('created_at', 'user_type')
    search_fields = ('first_name', 'last_name', 'phone')
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('first_name', 'last_name', 'user_type')
        }),
        ('Aloqa', {
            'fields': ('phone',)
        }),
        ('Xabar', {
            'fields': ('message',)
        }),
        ('Vaqt', {
            'fields': ('created_at',)
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone')
    fieldsets = (
        ('Aloqa ma\'lumotlari', {
            'fields': ('email', 'phone', 'address')
        }),
    )

    def has_add_permission(self, request):
        # Allow adding only if no instance exists
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)
