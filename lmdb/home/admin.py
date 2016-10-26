from django.contrib import admin

# Register your models here.

from home.models import Movies,Actor,Director

class MoviesAdmin(admin.ModelAdmin):
    list_display=('title','release_date','duration','director')
    search_fields=('title','release_date')
    list_filter=('release_date',)
    date_hierarchy=('release_date')
    ordering=('-release_date',)
admin.site.register(Movies,MoviesAdmin)
admin.site.register(Director)
admin.site.register(Actor)
