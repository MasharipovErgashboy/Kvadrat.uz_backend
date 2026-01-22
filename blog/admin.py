from django.contrib import admin
from .models import Blog, FeaturedBlog, RegularBlog

@admin.register(FeaturedBlog)
class FeaturedBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'is_featured')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'image')
        }),
        ('Muallifning ma\'lumotlari', {
            'fields': ('author', 'author_image')
        }),
        ('Kontenti', {
            'fields': ('content', 'read_time')
        }),
        ('Sozlamalar', {
            'fields': ('date', 'slug')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_featured=True)

    def save_model(self, request, obj, form, change):
        obj.is_featured = True
        super().save_model(request, obj, form, change)

@admin.register(RegularBlog)
class RegularBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'is_featured')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'image')
        }),
        ('Muallifning ma\'lumotlari', {
            'fields': ('author', 'author_image')
        }),
        ('Kontenti', {
            'fields': ('content', 'read_time')
        }),
        ('Sozlamalar', {
            'fields': ('date', 'slug')
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_featured=False)

    def save_model(self, request, obj, form, change):
        obj.is_featured = False
        super().save_model(request, obj, form, change)
