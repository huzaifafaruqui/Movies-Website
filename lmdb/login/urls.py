from django.conf.urls import url
from django.contrib import admin
import login.views
#from .import views

urlpatterns=[
    url(r'^$',login.views.log_in),
    url(r'^index.html/$',login.views.redirect),
    
]
