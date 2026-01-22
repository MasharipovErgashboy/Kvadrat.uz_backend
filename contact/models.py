from django.db import models

class ContactSubmission(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ismi")
    last_name = models.CharField(max_length=100, verbose_name="Familiyasi")
    user_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Turi")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami")
    message = models.TextField(blank=True, null=True, verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqti")

    class Meta:
        verbose_name = "Murojaat"
        verbose_name_plural = "Murojatlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ContactInfo(models.Model):
    email = models.EmailField(default="emlakuzinfo@gmail.com", verbose_name="Email")
    phone = models.CharField(max_length=50, default="+998 (20) 017-57-53", verbose_name="Telefon raqami")
    address = models.TextField(default="123 Fintech Avenue, Suite 400\nSan Francisco, CA 94105, USA", verbose_name="Manzili")

    class Meta:
        verbose_name = "Aloqa ma'lumotlari"
        verbose_name_plural = "Aloqa ma'lumotlari"

    def __str__(self):
        return "Aloqa sahifasining ma'lumotlari"

    def save(self, *args, **kwargs):
        if not self.pk and ContactInfo.objects.exists():
            # If you want to ensure only one instance exists
            return
        super(ContactInfo, self).save(*args, **kwargs)
