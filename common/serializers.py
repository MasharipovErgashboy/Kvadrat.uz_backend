from rest_framework import serializers
from .models import PrivacyPolicy, AboutUs, ForWhom, Testimonial

class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class ForWhomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForWhom
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
