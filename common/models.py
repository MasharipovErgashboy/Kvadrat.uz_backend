from django.db import models

class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255, default="Maxfiylik siyosati")
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Maxfiylik siyosati"
        verbose_name_plural = "Maxfiylik siyosati"


class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name="Rasm")
    order = models.IntegerField(default=0, verbose_name="Tartibi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda"
        ordering = ['order']


class ForWhom(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    icon = models.CharField(max_length=100, blank=True, verbose_name="Ikonka", help_text="Bootstrap ikonka yoki emoji")
    order = models.IntegerField(default=0, verbose_name="Tartibi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kimlar uchun"
        verbose_name_plural = "Kimlar uchun"
        ordering = ['order']


class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism")
    position = models.CharField(max_length=255, blank=True, verbose_name="Lavozimi")
    company = models.CharField(max_length=255, blank=True, verbose_name="Kompaniya")
    text = models.TextField(verbose_name="Matn")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True, verbose_name="Rasm")
    rating = models.IntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Reyting")
    order = models.IntegerField(default=0, verbose_name="Tartibi")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    def __str__(self):
        return f"{self.name} - {self.company}"

    class Meta:
        verbose_name = "Testimoniyal"
        verbose_name_plural = "Testimoniyallar"
        ordering = ['order']
