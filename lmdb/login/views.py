from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from .models import userlogin
from signup.models import users
# Create your views here.
def log_in(request):
	
	form = PostForm(request.POST or None)
	if form.is_valid():
		f1=form.cleaned_data['user_name']
		f2=form.cleaned_data['password']
		context={
		"user":f1
		}
		queryset=users.objects.all()
		for obj in queryset:
			if f1==obj.user_name and f2==obj.password:
				return render(request,"index.html",context)


	context={
		"form":form,
	}
	return render(request, "login.html", context)
def redirect(request):
	context={}
	return render(request,"templates/index.html",context)

