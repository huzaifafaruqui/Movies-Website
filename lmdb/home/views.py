from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse


# Create your views here.

def base(request):
	context={
		
	}
	return render(request, "index.html", context)
