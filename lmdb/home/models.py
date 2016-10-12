from __future__ import unicode_literals

from django.db import models

# Create your models here.
class movies(models.Model):
	title=models.CharField(max_length=30)
	release_date=models.DateField()
	image=models.ImageField()
	movie_id=models.IntegerField()
	duration=models.DurationField()


