from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return render(request, 'accountapp/hello_world.html')
    #return HttpResponse('hello_world') # 웹페이지에서 보이는 컨텐츠를 정해준다!
