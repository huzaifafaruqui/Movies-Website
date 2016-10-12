from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns=[
    url(r'^$',"signup.views.sign_in"),
    url(r'^users/$',"signup.views.display"),
    url(r'^conform.html/$',"signup.views.redirect"),
    
]