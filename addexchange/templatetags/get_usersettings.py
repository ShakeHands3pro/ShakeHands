from django import template
from django.contrib.auth import get_user_model
from accounts.models import(
    UserSetting
)
User=get_user_model()
register = template.Library()
 
@register.filter
def get_displayname(id):
    user = User.objects.get(pk=id)
    user_setting = UserSetting.objects.get(user=user)
    if user_setting.display_name:
        return user_setting.display_name
    return user.get_full_name()

@register.filter
def get_iconpic_url(id):
    user = User.objects.get(pk=id)
    user_setting = UserSetting.objects.get(user=user)
    if user_setting.icon_pic:
        print(user_setting.icon_pic.url)
        return user_setting.icon_pic.url
    return None

@register.filter
def get_course(id):
    user = User.objects.get(pk=id)
    user_setting = UserSetting.objects.get(user=user)
    if user_setting.course:
        return user_setting.get_course_display()
    return "所属学科未登録"

@register.filter
def get_graduationyear(id):
    user = User.objects.get(pk=id)
    user_setting = UserSetting.objects.get(user=user)
    if user_setting.graduation_year:
        return str(user_setting.graduation_year)+"卒"
    return "卒業年度未登録"

@register.filter
def get_email(id):
    user = User.objects.get(pk=id)
    return user.email
