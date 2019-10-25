from django import forms
from django.contrib.auth import get_user_model
from .models import (
   addressExchange
)
from accounts.models import (
    UserSetting
)
from pprint import pprint

User=get_user_model()

class addex_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['request_time'].required = False
    class Meta:
        model=addressExchange
        fields=(
            'text',
            'request_time',
        )
    def is_valid(self):
        print(self.errors)
        return super(addex_form, self).is_valid()

