from rest_framework import viewsets, mixins
from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer

class ContactSubmissionViewSet(mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

from .models import ContactInfo
from .serializers import ContactInfoSerializer

class ContactInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
