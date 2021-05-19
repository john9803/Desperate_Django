from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView

# 경로지정

app_name = "accountapp" # 브라우저에서 접근할때 ip가 아니라 app_name으로 들어올 수 있게 해준다!!

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'), # class based view 일때 작성법!!

]