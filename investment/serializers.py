from rest_framework import serializers
from .models import InvestmentStat, TeamMember

class InvestmentStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentStat
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'
