from django.contrib import admin
from .models import InvestmentStat, TeamMember

@admin.register(InvestmentStat)
class InvestmentStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order')
    list_editable = ('order',)
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('label', 'value', 'icon_name')
        }),
        ('Ranglar', {
            'fields': ('bg_color', 'text_color')
        }),
        ('Sozlamalar', {
            'fields': ('order',)
        }),
    )

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('name', 'role', 'image')
        }),
    )
