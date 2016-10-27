from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from home.models import Movie

# Create your views here.

def base(request):
	movies=Movie.objects.all()
	
	context={
		'movies':movies
	}
	return render(request, "index.html", context)
