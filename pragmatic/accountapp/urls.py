from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp" # 브라우저에서 접근할때 ip가 아니라 app_name으로 들어올 수 있게 해준다!!



urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

]