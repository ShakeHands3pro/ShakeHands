from django import forms
from .models import Question,QIndex,Answer,Like


class Question_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['index']=forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            required=True,
            queryset=QIndex.objects
        )
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Question
        fields = (
            'title',
            'text',
            'index',
        )

class Answer_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['advice'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Answer
        fields = (
            'advice',
        )

class Like_form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Like
        fields=(
            'answer',
            'user',
        )
    def save(self):
        like = super(Like_form,self).save()
        print("save()が実行されました")
        return like