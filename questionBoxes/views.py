from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.views import generic
from django.forms import modelformset_factory
from .models import Question,QIndex,Answer,Like
from .forms import Question_form,Answer_form,Like_form
from accounts.models import User 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from dateutil.relativedelta import relativedelta
import datetime 
from django.db.models import Q


# Create your views here.

class CreateQuestionView(LoginRequiredMixin, generic.CreateView):
    model = Question
    form_class=Question_form
    template_name = 'questionBoxes/createform.html'
    success_url = reverse_lazy('mypage:top')
    def form_valid(self, form):
        result = form.save(commit=False)
        result.answerer=get_object_or_404(User,pk=self.kwargs['id'])
        result.questionner=get_object_or_404(User,pk=self.request.user.id)
        result.save()
        return super(CreateQuestionView, self).form_valid(form)



class AnswerView(LoginRequiredMixin, generic.CreateView):
    #questionBoxes/answer/post_pk 回答投稿.
    model = Answer
    form_class=Answer_form
    template_name = 'questionBoxes/answer.html'
    success_url = reverse_lazy('mypage:top')
    def form_valid(self, form):
        question_pk = self.kwargs['id']
        question = get_object_or_404(Question, id=question_pk)
        question.status=2
        question.save()
        # 紐づく記事を設定する
        advice = form.save(commit=False)
        advice.question = question
        advice.save()
        return super(AnswerView, self).form_valid(form)  
    def get_context_data(self,**kwargs):
        context = super(AnswerView, self).get_context_data(**kwargs)
        context['advice']=q_model=get_object_or_404(Question, id=self.kwargs['id'])
        return context



class list(LoginRequiredMixin, generic.TemplateView):
    template_name='questionBoxes/list.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        login_user = self.request.user
        today=datetime.date.today()+relativedelta(days=1)
        threemonths_ago=today-relativedelta(months=3)

        #自分がした質問のうち、回答されたもの
        answered_by = Question.objects.filter(questionner=login_user, status=2)
        #自分がした質問全て
        allQ_IAskedFor = Question.objects.filter(questionner=login_user)
        #誰かにされた質問の全て
        allQ_IWasAsked = Question.objects.filter(answerer=login_user)
        #誰かにされた質問のうち、まだ回答していないもの
        I_unanswered = Question.objects.filter(answerer=login_user, status=1).filter(created_at__range=(threemonths_ago,today))
        context.update({
            'answered_by':answered_by,#回答された
            'allQ_IAskedFor':allQ_IAskedFor,#自分がした質問全て
            'allQ_IWasAsked':allQ_IWasAsked,#誰かにされた質問の全て
            'I_unanswered':I_unanswered,#まだ回答していない
        })
        return context


class QBoxView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'questionBoxes/QboxInfo.html'
    form_class=Like_form
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        question_pk = self.kwargs['id']
        question = get_object_or_404(Question, id=question_pk)
        try:
            ans = Answer.objects.filter(question=question)
        except Answer.DoesNotExist:
            ans = None
        
        if ans != None:
            try:
                like_count = Like.objects.filter(answer=ans[0]).count()
            except Like.DoesNotExist:
                like_count = 0
            try:
                like_status = True if Like.objects.filter(answer=ans[0], user=self.request.user).count()!=0 else False
            except Like.DoesNotExist:
                like_status = False
        else:
            lile_count=0
            like_status = False

        context.update({
            'question':question,
            'answer':ans[0],
            'like_count':like_count,
            'like_status':like_status,
        })
        return context

    def post(self, request, *args, **kwargs):
        status=int(request.POST.get('status',None))
        question = get_object_or_404(Question, id=self.kwargs['id'])
        ans = get_object_or_404(Answer, question=question)
        if status==1:
            #すでにライクボタンが押されているから、DELETEすれば良い
            #messages.warning(request, 'いいねを取り消しました')
            try:
                like = Like.objects.filter(answer=ans, user=self.request.user)
                like.delete()
            except:
                raise Http404
        elif status==0:
            #messages.success(request, 'いいね！しました')
            data={
                'user':self.request.user.id,
                'answer':ans.id
            }
            form = self.form_class(data=data)          
            if form.is_valid():
                form.save()
        return redirect('questionBoxes:detail',id=self.kwargs['id'])
        


    """ def like(request, *args, **kwargs):
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
class Search_question(generic.ListView):
    template_name='questionBoxes/search_questionbox.html'
    model = Answer
    #form=ProfileSearchForm
    paginate_by = 10
    def get_queryset(self):
        qs = Answer.objects.all()
        
        q_ans = self.request.GET.get('advice')
        q_tag = self.request.GET.getlist('tag')
        q_gakka=self.request.GET.get('gakka')

        if not len(q_tag)==0 and not len(q_ans)==0 and not len(q_gakka)==0:
            print("1")
            qs = qs.filter(
                Q(question__title__contains=q_ans)|Q(advice__contains=q_ans)|Q(question__text__contains=q_ans)|Q(question__index__in=q_tag)|Q(question__questionner__usersetting__course__contains=q_gakka)
                )
        elif not len(q_tag)==0 :
            print("2")
            qs= qs.filter(question__index__in=q_tag)
        
        elif q_ans is not None:
            print("3")
            qs = qs.filter(
                Q(question__title__contains=q_ans)|Q(advice__contains=q_ans)|Q(question__text__contains=q_ans)
                )
            qs = qs.filter(question__questionner__usersetting__course__contains=q_gakka)

        print(qs)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ques= Question.objects.all()
        context['ques'] = ques
        
        return context