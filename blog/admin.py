from django.contrib import admin
from .models import Blog, FeaturedBlog, RegularBlog

@admin.register(FeaturedBlog)
class FeaturedBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'is_featured')
    search_fields = ('title', 'description')
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_featured=True)

    def save_model(self, request, obj, form, change):
        obj.is_featured = True
        super().save_model(request, obj, form, change)

@admin.register(RegularBlog)
class RegularBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'is_featured')
    search_fields = ('title', 'description')

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_featured=False)

    def save_model(self, request, obj, form, change):
        obj.is_featured = False
        super().save_model(request, obj, form, change)

# Optionally keep the main Blog admin to see everything, or remove it.
# The user asked for specific forms, so having these two is the priority.
# I will keep the main one hidden or just these two.
# Let's unregister the main one if it was strictly "switch to this".
# But for safety/admin completeness, often "All" view is useful. 
# However, to avoid clutter ("Blog", "FeaturedBlog", "RegularBlog"), I will NOT register the base Blog model anymore
# so the user only sees the two distinct sections as requested.
