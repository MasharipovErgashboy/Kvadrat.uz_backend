from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Qisqacha tavsif")
    content = models.TextField(verbose_name="Toʻliq mazmun", help_text="Blog-postning toʻliq matni")
    image = models.ImageField(upload_to='blog/', verbose_name="Rasm")
    author = models.CharField(max_length=100, verbose_name="Muallifning ismi")
    author_image = models.ImageField(upload_to='blog/authors/', blank=True, null=True, verbose_name="Muallifning rasmi")
    date = models.DateField(verbose_name="Sana")
    read_time = models.CharField(max_length=20, default="5 min read", verbose_name="O'qish vaqti")
    is_featured = models.BooleanField(default=False, verbose_name="Tanlangan")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="URL manzili")

    class Meta:
        ordering = ['-date']
        verbose_name = "Blog va maqolalar"
        verbose_name_plural = "Blog va maqolalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class FeaturedBlog(Blog):
    class Meta:
        proxy = True
        verbose_name = "Tanlangan blog va maqolalar"
        verbose_name_plural = "Tanlangan blog va maqolalar"

class RegularBlog(Blog):
    class Meta:
        proxy = True
        verbose_name = "Oxirgi blog, yangiliklar va maqolalar"
        verbose_name_plural = "Oxirgi blog, yangiliklar va maqolalar"
