from django.shortcuts import render
from django.http import HttpResponse
from .models import Reviews

books = [
    {
        'title': 'Lord of the Rings',
        'author': 'J.R.R.Tolkien',
        'rating': '10/10'
    }
]


def home(request):
    return render(request, 'Grantha/home.html')


def about(request):
    return render(request, 'Grantha/about.html')


def browse(request):

    context = {
        'objects':Reviews.objects.all()
    }
    return render(request,'Grantha/browse2.html',context)
