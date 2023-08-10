from django.contrib import admin
from .models import Blog, History, Person

# Register your models here.
# admin.site.register(Blog)
admin.site.register(History)


@admin.register(Blog) 
class BlogAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'text')

@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')

