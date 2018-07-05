# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(max_length=140)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.content)

	# success url or goes to get_absolute_url defined
	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs={"pk":self.pk})