from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    num = Friend.object.all().count()
    first = Friend.objects.all().first()
    last = Friend.object.all().last()
    data = [num, first, last]
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)