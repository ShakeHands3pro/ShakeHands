from django import form_class
from users.models import Question

class QuestionForm(form.ModelForm):
    class Meta:
        model = Question
        Formfields = ['title', 'question', 'index']
    def __init__(self, *args, **kwargs):
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトル'
        self.fields['title'].widget.attrs['maxlength'] = '50'
        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['placeholder'] = '質問文'
        self.fields['text'].widget.attrs['maxlength'] = '300'
        ""tag""

 """ form_class=QuestionForm
    template_name = 'questionBoxes/question/create.html'
    success_url = reverse_lazy('users:question') """

    """ def from_valid(self, form):
        result =super().form_valid(form)
        message.success(
            self.request, '「{}」を作成'.format(form.instance))
        return result """
    