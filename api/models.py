# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=100, null=True)
    creation = models.DateField(null=True)
    last_edit = models.DateField(null=True)
    title = models.CharField(max_length=500, null=True)
    content = models.TextField(null=True)

    def __unicode__(self):
        return self.title
