from django.contrib import admin

# Register your models here.

from home.models import Movie,Actor,Director

class MovieAdmin(admin.ModelAdmin):
    list_display=('title','release_date','duration','director')
    search_fields=('title','release_date')
    list_filter=('release_date',)
    date_hierarchy=('release_date')
    ordering=('-release_date',)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Director)
admin.site.register(Actor)
