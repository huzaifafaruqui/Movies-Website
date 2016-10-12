from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def base(request):
	context={
		
	}
	return render(request, "index.html", context)
