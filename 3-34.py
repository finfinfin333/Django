from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
#from .forms import HelloForm
from .forms import FriendForm #この文を新たに追記

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

#create model
# from .forms import HelloForm #この文を削除する


def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }

    return render(request, 'hello/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num) #インスタンスの取得
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save() #更新されたレコードの保存
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)