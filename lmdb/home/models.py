from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Actor(models.Model):
	first_name=models.CharField(max_length=30,default='huzaifa')
	last_name=models.CharField(max_length=40,default='faruqui')
	age=models.IntegerField(default='20')
	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)
	
class Director(models.Model):
	first_name=models.CharField(max_length=30,default='huzaifa')
	last_name=models.CharField(max_length=40,default='faruqui')
	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Movie(models.Model):
	title=models.CharField(max_length=30)
	release_date=models.DateField()
	actors=models.ManyToManyField(Actor)
	director=models.ForeignKey(Director)
	image=models.ImageField(upload_to = 'static/images/products', default = 'pictures/movie2.jpg')
	duration=models.DurationField()
	def __str__(self):
		return u'%s' % (self.title)

