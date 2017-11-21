# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def validate(self, data):
		errors = []
		if len(data["email"]) == 0:
			errors.append("please put in an email")
		if len(data["password"]) < 7:
			errors.append("please put in a password greater than 8 characters")
		if len(errors) == 0:
			return True,
		if len(errors) > 0:
			return False, errors


class User(models.Model):
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	def display_info(self):
		print self.email
		print self.password


