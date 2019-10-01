from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'questionBoxes'

urlpatterns = [
    #path('', views.Top.as_view(), name='login'),
    path('questionBoxes/index', views.QboxIndex.as_view(), name='QboxIndex'),
    path('questionBoxe/<uuid>', views.QboxDetBox.as_view(), name='QboxDetBox'),
]