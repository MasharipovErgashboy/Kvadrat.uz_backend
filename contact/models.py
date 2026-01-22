from django.db import models

class ContactSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ContactInfo(models.Model):
    email = models.EmailField(default="emlakuzinfo@gmail.com")
    phone = models.CharField(max_length=50, default="+998 (20) 017-57-53")
    address = models.TextField(default="123 Fintech Avenue, Suite 400\nSan Francisco, CA 94105, USA")

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return "Contact Page Information"

    def save(self, *args, **kwargs):
        if not self.pk and ContactInfo.objects.exists():
            # If you want to ensure only one instance exists
            return
        super(ContactInfo, self).save(*args, **kwargs)
