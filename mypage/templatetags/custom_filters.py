from django import template
from django.contrib.auth import get_user_model
from accounts.models import(
    UserSetting
)

register = template.Library()
@register.filter

def name(querydict):
    name = querydict.get('name')
    
    return "" if name is None else name
