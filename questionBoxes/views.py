from django.shortcuts import render
from django.views import generic
from django.forms import modelformset_factory
from .models import Question,QIndex

# Create your views here.

class CreateQuestionView(generic.CreateView):
    model = Question
    form_class=QuestionForm
    template_name = "question_create_form.html"
    success_url = reverse_lazy('users:question')
 
    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を作成しました'.format(form.instance))
        return result
"""
class AnswerView(generic.CreateView):
    #questionBoxes/answer/post_pk 回答投稿.
    model = Answer
    fields = ('advice', 'answerer)
    template_name = 'questionBoxes/answer/post_pk.html'
 
    def form_valid(self, form):
        question_pk = self.kwargs['pk']
        question = get_object_or_404(Question, pk=queston_pk)
 
        # 紐づく記事を設定する
        advice = form.save(commit=False)
        advice.question = question
        advice.save()
        # 記事詳細にリダイレクト
        return redirect('QBoxInfo', pk=question_pk)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quesiton = self.request.question
        context['question'] = get_object_or_404(Question, pk=question_pk)
    return context

class QBoxView(    ):
    #質問箱一覧
    template_name = 'questionBoxes/QboxInfo.html'
    def QuestionView(request, post_id):
        Qbox = Question.objects.get(pk=post_id)
        return render(reqest, 'self.template_name', {'Qbox_id': post_id})


    def like(request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['question_id'])
        is_like = Like.objects.filter(user=request.user).filter(question=question).count()
    # unlike
    if is_like > 0:
        liking = Like.objects.get(question__id=kwargs['question_id'], user=request.user)
        liking.delete()
        question.like_num -= 1
        question.save()
        messages.warning(request, 'いいねを取り消しました')
        return redirect(reverse_lazy('questions:question_info', kwargs={'question_id': kwargs['question_id']}))
    # like
    question.like_num += 1
    question.save()
    like = Like()
    like.user = request.user
    like.question = question
    like.save()
    messages.success(request, 'いいね！しました')
    return HttpResponseRedirect(reverse_lazy('questions:question_detail', kwargs={'question_id': kwargs['question_id']}))

 """