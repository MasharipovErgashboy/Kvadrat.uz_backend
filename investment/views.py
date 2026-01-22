from rest_framework import viewsets
from .models import InvestmentStat, TeamMember
from .serializers import InvestmentStatSerializer, TeamMemberSerializer

class InvestmentStatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvestmentStat.objects.all()
    serializer_class = InvestmentStatSerializer

class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
