from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    #path('', views.Top.as_view(), name='login'),
    path('', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.UserCreate.as_view(),name='signup'),
    path('signup/done/', views.UserCreateDone.as_view(),name='signup_done'),
    path('signup/setting/<token>/', views.UserCreatesetting.as_view(),name='signup_setting'),
    path('signup/complete/', views.UserCreateComplete.as_view(),name='signup_complete'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('setting/',views.UserSettingUpdate.as_view(),name='accountsSetting'),
    path('setting/icon',views.iconPic_change.as_view(),name='iconSetting'),
]