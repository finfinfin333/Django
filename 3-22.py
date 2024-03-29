from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from django.db.models import QuerySet

def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + '</td>'
        result += '</tr>'
    return result

QuerySet.__str__ = __new_str__

def index(request):
    data = Friend.object.all().values('id', 'name', 'age')
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)