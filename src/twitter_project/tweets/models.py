# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.conf import settings

from .validators import validate_content

# validation on input textfield
# def validate_content(value):
# 	content = value
# 	if content == "abc":
# 		raise ValidationError("Content cannot be ABC or abc")
# 	return value

# Create your models here.
class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(max_length=140, validators=[validate_content])
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.content)

	# success url or goes to get_absolute_url defined
	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs={"pk":self.pk})

	#validation on whole object
	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == "abc":
	# 		raise ValidationError("Content cannot be ABC")
	# 	return super(Tweet, self).clean(*args, **kwargs)