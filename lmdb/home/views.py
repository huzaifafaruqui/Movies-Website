from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from home.models import Movie
from django.contrib.auth import logout
from home.forms import *
from django.contrib import messages
# Create your views here.

from django.shortcuts import render


    
def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
        if not q:
        	error=True
        else:
        	movies = Movie.objects.filter(title__icontains=q)
        	return render(request, 'search_results.html',
                      {'movies': movies, 'query': q})
	if error==True:	
		messages.error(request, "Enter something!")
	return HttpResponseRedirect('/')
    
def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email'])
			return HttpResponseRedirect('/')
	else:
		form = RegistrationForm()
	#variables = RequestContext(request, {'form': form})
	#return render_to_response('registration/register.html',variables)
	return render(request,'registration/register.html',({'form':form}))
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')


def base(request):
	movies=Movie.objects.all()
	
	context={
		'movies':movies,
		'user': request.user
	}
	return render(request, "index.html", context)
def movie_page(request, id):
	movie=get_object_or_404(Movie,id=id)
	context={
	'movie': movie
	}
	return render(request,"movie.html",context)
	
def add_comment_to_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return HttpResponseRedirect('/movie/%d/'%movie.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_movie.html', {'form': form})	
