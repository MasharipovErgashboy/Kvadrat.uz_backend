from django.contrib import admin
from .models import PrivacyPolicy

@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
