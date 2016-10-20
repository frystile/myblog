from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    blog = models.ForeignKey('blogs.Blog')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post_detail', kwargs={'blog': self.blog.id, 'pk': self.id})

class Blog(models.Model):
    author = models.ForeignKey('core.User', default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('blogs.Category')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post_list', kwargs={'pk': self.id})

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    hashtag = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.hashtag
