from django.db import models

class InvestmentStat(models.Model):
    icon_name = models.CharField(max_length=50, help_text="Available: Calendar, Users, TrendingUp, Wallet, BarChart3, etc.")
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    bg_color = models.CharField(max_length=50, default="bg-blue-50")
    text_color = models.CharField(max_length=50, default="text-blue-600")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name
