from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'questionBoxes'

urlpatterns = [
    #path('', views.Top.as_view(), name='login'),
    path('create/<uuid:id>', views.CreateQuestionView.as_view(), name='create'),
    path('answer/<uuid:id>', views.AnswerView.as_view(), name='answer'),
    path('list/',views.list.as_view(),name='list'),
    path('detail/<uuid:id>', views.QBoxView.as_view(),name='detail')
]