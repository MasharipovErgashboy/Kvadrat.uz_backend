from django.db import models

class FAQ(models.Model):
    TYPE_CHOICES = (
        ('home', 'Asosiy sahifa'),
        ('investment', 'Investisiya sahifasi'),
    )
    question = models.CharField(max_length=255, verbose_name="Savol")
    answer = models.TextField(verbose_name="Javob")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='home', verbose_name="Turi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartibi")

    class Meta:
        ordering = ['order']
        verbose_name = "Savol va javoblar"
        verbose_name_plural = "Savol va javoblar"

    def __str__(self):
        return self.question
