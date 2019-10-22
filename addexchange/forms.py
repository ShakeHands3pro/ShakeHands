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

    class Meta:
        model=addressExchange
        fields=(
            'text',
            'request_time',
        )

