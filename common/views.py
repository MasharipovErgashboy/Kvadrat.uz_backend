from rest_framework import viewsets
from .models import PrivacyPolicy, AboutUs, ForWhom, Testimonial
from .serializers import PrivacyPolicySerializer, AboutUsSerializer, ForWhomSerializer, TestimonialSerializer

class PrivacyPolicyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer


class AboutUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class ForWhomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ForWhom.objects.all()
    serializer_class = ForWhomSerializer


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
