from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'type', 'order')
    list_filter = ('type',)
    search_fields = ('question', 'answer')
    list_editable = ('order',)
    fieldsets = (
        ('Savol va javob', {
            'fields': ('question', 'answer')
        }),
        ('Sozlamalar', {
            'fields': ('type', 'order')
        }),
    )
