from django.shortcuts import redirect,render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import(
    addex_form
)
from .models import(
    addressExchange
)
from accounts.models import(
    User,UserSetting
)
import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Q

# Create your views here.
class addExc(LoginRequiredMixin,generic.UpdateView):
    model=addressExchange
    template_name='addexchange/addExc_form.html'
    form_class=addex_form
    success_url=reverse_lazy('mypage:top')#後で直す
    def get_object(self,**kwargs):
        login_user=self.request.user
        to_user=User.objects.get(id=self.kwargs['id'])#相手のユーザー
        try:
            obj=addressExchange.filter(questioner=login_user,answerer=to_user)
            #状態が拒否の時の場合を書き足す、リダイレクトさせる
        except:
            obj=addressExchange()
            obj.questioner=login_user
            obj.answerer=to_user
        return obj

class addExchange_list(LoginRequiredMixin, generic.TemplateView):
    template_name='addexchange/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_user = self.request.user
        today=datetime.date.today()
        threemonths_ago=today-relativedelta(months=3)
        #まだ返事が来ていないもの
        waiting = addressExchange.objects.filter(questioner=login_user).exclude(approve_boolean=True and False).filter(request_time__range=(threemonths_ago, today))      
        #申請して連絡先交換が成立したもの
        accepted = addressExchange.objects.filter(Q(questioner=login_user), Q(approve_boolean=True)|Q(answerer=login_user), Q(approve_boolean=True))
        #申請されてまだ返事をしていないもの
        offered = addressExchange.objects.filter(answerer=login_user).filter(request_time__range=(threemonths_ago, today)) 
        context.update({
            'waiting':waiting,
            'accepted':accepted,
            'offered':offered,
        })
        return context

class detail(LoginRequiredMixin, generic.TemplateView):
    template_name='addexchange/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exchangeModel=addressExchange.objects.get(id=self.kwargs['id'])
        print(exchangeModel.id)
        #user_idはアドレス交換申請をした人、された人のうち、ログインユーザじゃない方を返している
        context['user_id'] = exchangeModel.answerer.id if exchangeModel.questioner==self.request.user else exchangeModel.questioner.id
        context.update({
            'model':exchangeModel,
        })
        return context

