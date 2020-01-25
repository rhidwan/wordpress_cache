from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.IntegerField(null=False)
    created_at = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    link = models.URLField()
    content = models.TextField()
    excerpt = models.TextField()

