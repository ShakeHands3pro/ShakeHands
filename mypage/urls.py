from . import views
from django.urls import path, include
#from django.contrib.auth import views as auth_views

app_name = 'mypage'

urlpatterns = [
    path('', views.top.as_view(), name='top'),
]