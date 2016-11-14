from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from home.models import Movie
from django.contrib.auth import logout
from home.forms import *
from django.contrib import messages
from django.db.models import Avg
# Create your views here.

from django.shortcuts import render

def advanced(request):
	form=SearchForm(request.POST or None)
	form2=SearchForm2(request.POST or None)
	#print request.POST.getlist('genres')
	#print form['minr'].value()
	#print form.cleaned_data['minr']
	if form.is_valid() and form2.is_valid():
		f1=form.cleaned_data['title'].lower()
		f2=form.cleaned_data['actors']
		min_rating=form.cleaned_data['minr']
		max_rating=form.cleaned_data['maxr']
		context={
		"title":f1
		,'actors':f2
		}
		queryset=Movie.objects.filter(title__icontains=f1)
		
		return render(request,"x.html",context)
		#for obj in queryset:
		#	if obj.title and f2==obj.:
				#return render(request,"index.html",context)

	context={
    'form':form,'form2':form2

    }
	return render(request,"advanced_search.html",context)

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
			email=form.cleaned_data['email'],
			first_name=form.cleaned_data['name'])
			
			return HttpResponseRedirect('/')
	else:
		form = RegistrationForm()
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
	#avg_stars = movie.objects.annotate(Avg('rating__stars'))
	
	context={
	'movie': movie,
	#'stars':avg_stars
	}
	return render(request,"movie.html",context)

def list_comments(request,id):
	movie=get_object_or_404(Movie,id=id)
	#avg_stars = movie.objects.annotate(Avg('rating__stars'))
	
	context={
	'movie': movie,
	#'stars':avg_stars
	}
	return render(request,"all_comments.html",context)
	
def add_comment_to_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    x=Comment.objects.filter(movie=movie,author=request.user)
    if len(x)>0:
		messages.error(request, "User already commented!")
		return HttpResponseRedirect('/movie/%d/'%movie.id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect('/movie/%d/'%movie.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_movie.html', {'form': form})	
