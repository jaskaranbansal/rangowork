from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context = context_dict)
    return HttpResponse("Rango says hey there partner!")

def about(request):
    context_dict = {'boldmessage': "Hello!"}
    return render(request, 'rango/about.html', context = context_dict)
    return HttpResponse("Rango says this is the about page!")
