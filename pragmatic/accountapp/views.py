from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

@login_required
def hello_world(request):

    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            new_hello_world= HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            hello_world_list = HelloWorld.objects.all()
            return HttpResponseRedirect(reverse('accountapp:login'))
        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/login', context={'hello_world_list': hello_world_list})
        #return HttpResponse('hello_world') # 웹페이지에서 보이는 컨텐츠를 정해준다!
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm # 기본적인 사용자 검증과정
    success_url = reverse_lazy('accountapp:login') #인증을 마치면 어리로 사용자를 돌려보낼 것인지를 알려주는코드
    # 위의 Http에서의 reverse와 바로윗줄에 reverse_lazy는 무엇이 다른가? -> 함수와 클래스가 불러오는 방식의 차이로 클래스를 불러오려면 reverse_lazy를 사용함
    template_name = 'accountapp/create.html'
    # 회원가입을 할때 어떤 html 파일을 보여줄 것인지를 지정해야함.

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user' # 개인페이지의 유저를 바꿔주기위한 코드
    template_name = 'accountapp/detail.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)



class UserUpdateForm(object):
    pass

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
# -> 일반 function에서 사용하는 decorator를 method에서 사용할 수 있게 하는 decorator
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm # 기본적인 사용자 검증과정
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'