from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blogs/posts/%i/" % self.id
