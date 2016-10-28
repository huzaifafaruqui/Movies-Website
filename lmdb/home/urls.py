from django.conf.urls import url
from django.contrib import admin
import home.views
#from .import views
urlpatterns=[
    url(r'^$',home.views.base),

]
