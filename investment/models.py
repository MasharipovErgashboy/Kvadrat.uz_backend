from django.db import models

class InvestmentStat(models.Model):
    icon_name = models.CharField(max_length=50, verbose_name="Ikonka nomi", help_text="Mavjud: Calendar, Users, TrendingUp, Wallet, BarChart3, va boshqalar.")
    value = models.CharField(max_length=50, verbose_name="Qiymat")
    label = models.CharField(max_length=100, verbose_name="Nomi")
    bg_color = models.CharField(max_length=50, default="bg-blue-50", verbose_name="Fon rangi")
    text_color = models.CharField(max_length=50, default="text-blue-600", verbose_name="Matn rangi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartibi")

    class Meta:
        ordering = ['order']
        verbose_name = "Investisiya statistikasi"
        verbose_name_plural = "Investisiya statistikasi"

    def __str__(self):
        return self.label

class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    role = models.CharField(max_length=100, verbose_name="Lavozimi")
    image = models.ImageField(upload_to='team/', verbose_name="Rasm")

    class Meta:
        verbose_name = "Jamoa a'zosi"
        verbose_name_plural = "Jamoa a'zolari"
        ordering = ['name']

    def __str__(self):
        return self.name
