from django import template
from django.contrib.auth import get_user_model
from accounts.models import(
    UserSetting,
    User
)
from questionBoxes.models import(
    Answer,
    Question
    
)

register = template.Library()
@register.filter

def checked(value, querydict):
    tags = querydict.getlist('tag')
    if str(value) in tags:
        return "checked"
    #return ""

def ans(querydict):
    ans = querydict.get('ans')
    
    return "" if ans is None else ans

def gakka(querydict):
    gakka = querydict.get('gakka')
    
    #return "" if gakka is None else gakka