from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
	user_name=models.CharField(max_length=50)
	full_name=models.CharField(max_length=60)
	email_id=models.CharField(max_length=50)
	password=models.CharField(max_length=100)

	def __unicode__(self):
		return self.user_name
	def __str__(self):
		return self.user_name

	
	
