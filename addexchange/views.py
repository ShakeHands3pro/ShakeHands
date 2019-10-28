from django.shortcuts import redirect,render,Http404
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
        obj=addressExchange.objects.filter(questioner=login_user,answerer=to_user).first()
        if(obj is None):
            obj=addressExchange()
            obj.questioner=login_user
            obj.answerer=to_user
        return obj
    

class addExchange_list(LoginRequiredMixin, generic.TemplateView):
    template_name='addexchange/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_user = self.request.user
        today=datetime.date.today()+relativedelta(days=1)
        threemonths_ago=today-relativedelta(months=3)
        #まだ返事が来ていないもの
        waiting = addressExchange.objects.filter(questioner=login_user).filter(approve_boolean=None).filter(request_time__range=(threemonths_ago, today))      
        #申請して連絡先交換が成立したもの
        accepted = addressExchange.objects.filter(Q(questioner=login_user,approve_boolean=True)|Q(answerer=login_user, approve_boolean=True))
        #申請されてまだ返事をしていないもの
        offered = addressExchange.objects.filter(answerer=login_user).filter(approve_boolean=None).filter(request_time__range=(threemonths_ago, today)) 
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
        #user_idはアドレス交換申請をした人、された人のうち、ログインユーザじゃない方を返している
        context['user_id'] = exchangeModel.answerer.id if exchangeModel.questioner==self.request.user else exchangeModel.questioner.id
        context.update({
            'model':exchangeModel,
        })
        return context

class confirm(LoginRequiredMixin,generic.TemplateView):
    template_name='addexchange/approve_waiting.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exchangeModel=addressExchange.objects.get(id=self.kwargs['id'])
        #user_idはアドレス交換申請をした人、された人のうち、ログインユーザじゃない方を返している
        context['user_id'] = exchangeModel.answerer.id if exchangeModel.questioner==self.request.user else exchangeModel.questioner.id
        context.update({
            'model':exchangeModel,
        })
        return context
    def get(self, request, *args, **kwargs):
        return super(confirm, self).get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        state_param=int(request.POST.get('state',None))
        if request.POST.get('model_id',None):
            model=addressExchange.objects.get(pk=request.POST.get('model_id',None))
        else:
            raise Http404
        if state_param==0:
            model.approve_boolean=False
            model.save()
        elif state_param==1:
            model.approve_boolean=True
            model.save()
        return redirect('addexchange:list')

            
            



