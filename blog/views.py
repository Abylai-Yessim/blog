from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.


# request
# Response

# 1) functions base 
# 2) class based 

menu = [
    {'title': 'Home', 'url': 'home'},
    {'title': 'About us', 'url': 'about'},
    {'title': 'Contacts', 'url': 'contact'},
]

def index(request):
    # Person.objects.create(name='Damir', age='22')
    # p = Person.objects.get(id=4)


    data = {
        'title': 'Главная', 
        'menu': menu, 
        'people': Person.objects.all().order_by('name')
        # 'people': [Person.objects.filter(age__gte=18)] # gte >= ////\\\\ #lte <=18
        # 'people': [Person.objects.get(age=18)] # gte >= ////\\\\ #lte <=18

    }
    return render(request, 'blog/index.html', data) 

def about(request):
    data={
        'menu': menu
    }
    return render(request, 'blog/about.html', data)

def contact(request):
    return HttpResponse("Контакты")

