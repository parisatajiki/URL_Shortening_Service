from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    url = models.URLField(unique=True)
    short_url = models.CharField(unique=True, max_length=10, null=False, blank=False,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)
    def __str__(self):
        return self.url