from django.db import models

class FAQ(models.Model):
    TYPE_CHOICES = (
        ('home', 'Home Page'),
        ('investment', 'Investment Page'),
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='home')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question
