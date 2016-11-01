from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Avg



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
	#RATINGS=((5,5),(4,4),(3,3),(2,2),(1,1))
	genres=(('action','ACTION'),('comedy','COMEDY'),('romance','ROMANCE'),('thriller','THRILLER'),('drama','DRAMA'))
	title=models.CharField(max_length=30,blank=True)
	release_date=models.DateField(blank=True)
	actors=models.ManyToManyField(Actor,blank=True)
	director=models.ForeignKey(Director,blank=True,null=True)
	genre=models.CharField(max_length=30,choices=genres,default='drama',blank=True)
	image=models.ImageField(upload_to = 'static/images/products', default = 'pictures/movie2.jpg')
	duration=models.DurationField()
	@property #http://www.blog.pythonlibrary.org/2014/01/20/python-201-properties/
	def average_rating(self):  #http://stackoverflow.com/questions/28888399/aggregate-average-of-model-field-with-foreign-key-django-rest
		return int(Comment.objects.filter(movie__id=self.id).aggregate(Avg('rating')).values()[0])
	def __str__(self):
		return u'%s' % (self.title)

class Comment(models.Model):
	RATINGS=((5,5),(4,4),(3,3),(2,2),(1,1))
	movie = models.ForeignKey('home.Movie', related_name='comments')
	author = models.ForeignKey(User)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=True)
	rating=models.PositiveSmallIntegerField(default=5,choices=RATINGS)
	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text
