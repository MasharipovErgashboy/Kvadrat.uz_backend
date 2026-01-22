from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ViewSets
from common.views import PrivacyPolicyViewSet, AboutUsViewSet, ForWhomViewSet, TestimonialViewSet
from faq.views import FAQViewSet
from investment.views import InvestmentStatViewSet, TeamMemberViewSet
from blog.views import BlogViewSet
from contact.views import ContactSubmissionViewSet, ContactInfoViewSet

# Router Setup
router = routers.DefaultRouter()
router.register(r'privacy-policy', PrivacyPolicyViewSet, basename='privacy-policy')
router.register(r'about-us', AboutUsViewSet, basename='about-us')
router.register(r'for-whom', ForWhomViewSet, basename='for-whom')
router.register(r'testimonials', TestimonialViewSet, basename='testimonials')
router.register(r'faqs', FAQViewSet, basename='faqs')
router.register(r'investment-stats', InvestmentStatViewSet, basename='investment-stats')
router.register(r'investment-team', TeamMemberViewSet, basename='investment-team')
router.register(r'blogs', BlogViewSet, basename='blogs')
router.register(r'contacts', ContactSubmissionViewSet, basename='contacts')
router.register(r'contact-info', ContactInfoViewSet, basename='contact-info')

# Swagger Setup
schema_view = get_schema_view(
   openapi.Info(
      title="Kvadrat.uz API",
      default_version='v1',
      description="API documentation for Kvadrat.uz",
      contact=openapi.Contact(email="contact@kvadrat.uz"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
