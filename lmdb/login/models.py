from __future__ import unicode_literals

from django.db import models

# Create your models here.
class userlogin(models.Model):
	user_name=models.CharField(max_length=50)
	password=models.CharField(max_length=100)

	

	def __str__(self):
		return self.user_name



