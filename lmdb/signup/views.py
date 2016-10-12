from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import users

# Create your views here.


def sign_in(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("user_name")
		instance.save()
		return render(request,'index.html',{})
	context={
		"form":form,
	}
	return render(request, "Signup.html", context)
	#return HttpResponse("<h1>hello world</h1>")
def display(request):
	queryset = users.objects.all()
	context={
		"object_list": queryset
	}
	return render(request, "display.html", context)
def redirect(request):
	context={}
	return render(request,"conform.html",context)