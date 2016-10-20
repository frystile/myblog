from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey('core.User', default=1)
    text = models.TextField()
    post = models.ForeignKey('blogs.Post')
    created_at = models.DateTimeField(auto_now_add=True)
