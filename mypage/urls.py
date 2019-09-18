from . import views
from django.urls import path, include
#from django.contrib.auth import views as auth_views

app_name = 'mypage'

urlpatterns = [
    path('', views.top.as_view(), name='top'),

    #学生生活情報の編集ページ
    path('setting/univlife/',views.settingUnivLifeInfo.as_view(), name='univlife_setting'),
    path('setting/univlife/club/add/',views.addClub.as_view(), name='univlife_club_add'),
    path('setting/univlife/club/update/<int:id>',views.updateClub.as_view(), name='univlife_club_update'),
    path('setting/univlife/club/delete/<int:id>',views.deleteClub.as_view(), name='univlife_club_delete'),
    path('setting/univlife/openQ/add/',views.addopenQ.as_view(), name='univlife_openQ_add'),
    path('setting/univlife/openQ/update/<int:id>',views.updateOpenQ.as_view(), name='univlife_openQ_update'),
    path('setting/univlife/openQ/delete/<int:id>',views.deleteOpenQ.as_view(), name='univlife_openQ_delete'),

    #就活情報の編集ページ
    path('setting/jobhunting/',views.setting_jobHuntingInfo.as_view(), name='jobhunting_setting'),
    path('setting/jobhunting/startTime',views.jobHunting_startTime_view.as_view(), name='jobhunting_startTime'),
    path('setting/jobhunting/requestment',views.jobHunting_requestment_view.as_view(), name='jobhunting_requestment'),
    path('setting/jobhunting/internship/create',views.internshipRec_create.as_view(), name='jobhunting_internRec_create'),
    path('setting/jobhunting/internship/update/<uuid:id>',views.internshipRec_update.as_view(), name='jobhunting_internRec_update'),
    path('setting/jobhunting/internship/delete/<uuid:id>',views.internshipRec_delete.as_view(), name='jobhunting_internRec_delete'),
    path('setting/jobhunting/prospectiveEmployer/create',views.prospectiveEmployer_create.as_view(), name='jobhunting_prospectiveEmployer_create'),
    path('setting/jobhunting/prospectiveEmployer/update/<uuid:id>',views.prospectiveEmployer_update.as_view(), name='jobhunting_prospectiveEmployer_update'),
    path('setting/jobhunting/prospectiveEmployer/delete/<uuid:id>',views.prospectiveEmployer_delete.as_view(), name='jobhunting_prospectiveEmployer_delete'),
]