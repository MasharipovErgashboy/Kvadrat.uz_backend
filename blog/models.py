from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(help_text="Full content of the blog")
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='blog/authors/', blank=True, null=True)
    date = models.DateField()
    read_time = models.CharField(max_length=20, default="5 min read")
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ['-date']

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
        verbose_name = "Blogs And Articles (Featured)"
        verbose_name_plural = "Blogs And Articles (Featured)"

class RegularBlog(Blog):
    class Meta:
        proxy = True
        verbose_name = "Latest Blogs, News & Articles"
        verbose_name_plural = "Latest Blogs, News & Articles"
