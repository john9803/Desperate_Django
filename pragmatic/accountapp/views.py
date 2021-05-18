from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world= HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    #return HttpResponse('hello_world') # 웹페이지에서 보이는 컨텐츠를 정해준다!

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm # 기본적인 사용자 검증과정
    success_url = reverse_lazy('accountapp:hello_world') #인증을 마치면 어리로 사용자를 돌려보낼 것인지를 알려주는코드
    # 위의 Http에서의 reverse와 바로윗줄에 reverse_lazy는 무엇이 다른가? -> 함수와 클래스가 불러오는 방식의 차이로 클래스를 불러오려면 reverse_lazy를 사용함
    template_name = 'accountapp/create.html'
    # 회원가입을 할때 어떤 html 파일을 보여줄 것인지를 지정해야함.

