from django.contrib import admin
from django.utils.html import format_html
from .models import PrivacyPolicy, AboutUs, ForWhom, Testimonial


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'updated_at')
    ordering = ('order',)
    list_editable = ('order',)
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'image')
        }),
        ('Sozlamalar', {
            'fields': ('order',)
        }),
    )


@admin.register(ForWhom)
class ForWhomAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'updated_at')
    ordering = ('order',)
    list_editable = ('order',)
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'icon')
        }),
        ('Sozlamalar', {
            'fields': ('order',)
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'rating', 'is_active', 'order')
    list_filter = ('is_active', 'rating')
    ordering = ('order',)
    list_editable = ('is_active', 'order')
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('name', 'position', 'company', 'image')
        }),
        ('Sharhlar', {
            'fields': ('text', 'rating')
        }),
        ('Sozlamalar', {
            'fields': ('is_active', 'order')
        }),
    )
