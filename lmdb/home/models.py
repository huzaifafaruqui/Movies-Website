from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Actor(models.Model):
	first_name=models.CharField(max_length=30,blank=True)
	last_name=models.CharField(max_length=40,blank=True)
	age=models.IntegerField(default='20')
	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)
	
class Director(models.Model):
	first_name=models.CharField(max_length=30,blank=True)
	last_name=models.CharField(max_length=40,blank=True)
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

class Comment(models.Model):
    movie = models.ForeignKey('home.Movie', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
