from django.urls import path
from .views import Sign_up, Info, Log_in, Log_out

urlpatterns = [
    path('signup/', Sign_up.as_view(), name = 'sign_up'),
    path('', Info.as_view(), name="all_clients"),
    path('login/' , Log_in.as_view(), name='login'),
    path('logout/', Log_out.as_view(), name='logout'),
    ]