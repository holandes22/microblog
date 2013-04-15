from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Post(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, editable=False)  # updates date on creation
    updated_at = models.DateTimeField(auto_now=True, editable=False)  # updates date on save()
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField()
    published = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name='posts')

    class Meta:
        ordering = ['-created_at', 'title']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
