from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name ='addexchange'
urlpatterns=[
    path('request/<uuid:id>/',views.addExc.as_view(),name='request'),
    path('list/',views.addExchange_list.as_view(),name='list'),
    path('detail/<uuid:id>/',views.detail.as_view(),name='detail'),
    path('approve/<uuid:id>/',views.confirm.as_view(),name='confirm'),
]