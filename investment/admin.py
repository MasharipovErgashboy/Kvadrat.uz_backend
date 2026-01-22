from django.contrib import admin
from .models import InvestmentStat, TeamMember

@admin.register(InvestmentStat)
class InvestmentStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order')
    list_editable = ('order',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
