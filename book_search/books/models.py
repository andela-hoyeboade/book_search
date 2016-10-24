from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='books')
    pub_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title
