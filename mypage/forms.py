from django import forms
from django.contrib.auth import get_user_model
from .models import (
    club, openQ, openQ_ans,
    jobHunting_requestment, jobHunting_startTime,
    internshipRecommendation, prospectiveEmployer
)

User=get_user_model()

class club_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = club
        fields = (
            'club_name',
        )

class openQ_ans_addform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['openQ'].queryset = self.get_q()
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = openQ_ans
        fields= (
            'openQ',
            'ans',
        )
    def get_q(self):
        login_user = self.user
        if openQ.objects.count() <= openQ_ans.objects.filter(user = login_user).count():
            return openQ.objects.note()
        return openQ.objects.all().exclude(openq_ans__user=login_user)
        

class openQ_ans_updateform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.openq = kwargs.pop('openq')
        super().__init__(*args, **kwargs)
        self.fields['openQ'].queryset = self.get_q()
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = openQ_ans
        fields= (
            'openQ',
            'ans',
        )
    def get_q(self):
        login_user = self.user
        if openQ.objects.count() <= openQ_ans.objects.filter(user = login_user).count():
            return openQ.objects.note()
        selected=openQ.objects.all().filter(id=self.openq.id)
        choices=openQ.objects.all().exclude(openq_ans__user=login_user)
        return (selected|choices)


class jobHunting_requestment_form(forms.ModelForm):
    #就職の希望を書くやつ
    class Meta:
        model = jobHunting_requestment
        fields = (
            'industry',
            'occupation',
            'workplace',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['industry'].required = False
        self.fields['occupation'].required = False
        self.fields['workplace'].required = False
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    

class jobHunting_startTime_form(forms.ModelForm):
    #就職始めた時期を書くところ
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = jobHunting_startTime
        fields = (
            'season',
        )

class internshipRec_form(forms.ModelForm):
    #就職の希望を書くやつ
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['implessions'].required = False
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = internshipRecommendation
        fields = (
            'industry',
            'occupation',
            'company_name',
            'season',
            'period',
            'overView',
            'implessions',
        )

class prospectiveEmployer_form(forms.ModelForm):
    #就職の希望を書くやつ
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = prospectiveEmployer
        fields = (
            'industry',
            'occupation',
            'company_name',
        )
