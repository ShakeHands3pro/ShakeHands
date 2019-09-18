from django.shortcuts import redirect,render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import(
    club_form, openQ_ans_addform, openQ_ans_updateform,
    jobHunting_startTime_form, jobHunting_requestment_form,
    internshipRec_form, prospectiveEmployer_form
)
from .models import(
    club, openQ_ans, openQ_ans,
    industry, occupation, prospectiveEmployer,
    jobHunting_startTime, jobHunting_requestment,
    internshipRecommendation
)

# Create your views here.
class top(LoginRequiredMixin,generic.TemplateView):
    template_name = 'mypage/mypage.html'




"""
大学生活情報登録・変更・削除
"""
class settingUnivLifeInfo(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage/UserSetting/UnivLifeInfo.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_user = self.request.user
        try:
            myClub = club.objects.filter(user=login_user)
        except club.DoesNotExist:
            myClub = None
        try:
            openQ_and_myans = openQ_ans.objects.filter(user=login_user)
        except openQ_ans.DoesNotExist:
            openQ_and_myans = None
        context.update({
            'myclub':myClub,
            'openQ':openQ_and_myans,
        })
        return context

class addClub(LoginRequiredMixin, generic.CreateView):
    model = club
    form_class = club_form
    template_name = 'mypage/createOrUpdate.html'
    success_url = reverse_lazy('mypage:univlife_setting')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(addClub, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(addClub, self).get_context_data(**kwargs)
        context["h2text"]="所属しているサークルや部活を追加"
        return context

class addopenQ(LoginRequiredMixin, generic.CreateView):
    model = openQ_ans
    form_class = openQ_ans_addform
    template_name = 'mypage/createOrUpdate.html'
    success_url = reverse_lazy('mypage:univlife_setting')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(addopenQ, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(addopenQ, self).get_context_data(**kwargs)
        context["h2text"]="オープンクエスチョンを追加"
        return context
    def get_form_kwargs(self):
        kwargs = super(addopenQ, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class updateClub(LoginRequiredMixin, generic.UpdateView):
    model = club
    form_class = club_form
    template_name = 'mypage/createOrUpdate.html'
    success_url = reverse_lazy('mypage:univlife_setting')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(updateClub, self).form_valid(form)
    def get_object(self):
        obj=club.objects.get(id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(updateClub, self).get_context_data(**kwargs)
        context["h2text"]="所属しているサークルや部活を編集"
        return context

class updateOpenQ(LoginRequiredMixin, generic.UpdateView):
    model = openQ_ans
    form_class = openQ_ans_updateform
    template_name = 'mypage/createOrUpdate.html'
    success_url = reverse_lazy('mypage:univlife_setting')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(updateOpenQ, self).form_valid(form)
    def get_object(self):
        obj=openQ_ans.objects.get(id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(updateOpenQ, self).get_context_data(**kwargs)
        context["h2text"]="オープンクエスチョンを編集"
        return context
    def get_form_kwargs(self):
        kwargs = super(updateOpenQ, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['openq'] = openQ_ans.objects.get(id=self.kwargs['id']).openQ
        return kwargs

class deleteClub(LoginRequiredMixin, generic.DeleteView):
    model = club
    template_name = 'mypage/comfirmDel.html'
    success_url = reverse_lazy('mypage:univlife_setting')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(deleteClub, self).form_valid(form)
    def get_object(self):
        obj=club.objects.get(id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(deleteClub, self).get_context_data(**kwargs)
        context["h2text"]="所属しているサークルや部活を削除します"
        return context

class deleteOpenQ(LoginRequiredMixin, generic.DeleteView):
    model = openQ_ans
    template_name = 'mypage/comfirmDel.html'
    success_url = reverse_lazy('mypage:univlife_setting')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(deleteOpenQ, self).form_valid(form)
    def get_object(self):
        obj=club.objects.get(id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(deleteOpenQ, self).get_context_data(**kwargs)
        context["h2text"]="オープンクエスチョンを削除します"
        return context





"""
就活情報登録・変更・削除
"""
class setting_jobHuntingInfo(LoginRequiredMixin, generic.TemplateView):
    template_name='mypage/UserSetting/JobHuntingInfo.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        login_user=self.request.user
        try:
            req = jobHunting_requestment.objects.get(user=login_user)
        except :#jobHunting_requestment.models.DoesNotExist:
            req = None
        try:
            start = jobHunting_startTime.objects.get(user=login_user)
        except :#jobHunting_startTime.DoesNotExist:
            start = None
        try:
            internshipRec = internshipRecommendation.objects.filter(user=login_user)
        except internshipRecommendation.DoesNotExist:
            internshipRec = None
        try:
            prospectiveEmp = prospectiveEmployer.objects.filter(user=login_user)
        except prospectiveEmployer.DoesNotExist:
            prospectiveEmp = None
        context.update({
            'jobReqestment':req,
            'jobHunting_StartTime':start,
            'internshipRec':internshipRec,
            'prospectiveEmployer':prospectiveEmp,
        })
        return context

class jobHunting_requestment_view(LoginRequiredMixin, generic.UpdateView):
    model = jobHunting_requestment
    template_name='mypage/createOrUpdate.html'
    form_class = jobHunting_requestment_form
    success_url = reverse_lazy('mypage:jobhunting_setting')
    def get_object(self):
        login_user=self.request.user
        try:
            req = jobHunting_requestment.objects.get(user=login_user)
        except:
            req = jobHunting_requestment()
            req.user = login_user
        return req
    def get_context_data(self, **kwargs):
        context = super(jobHunting_requestment_view, self).get_context_data(**kwargs)
        context['h2text']="就職希望を登録する"
        return context

class jobHunting_startTime_view(LoginRequiredMixin, generic.UpdateView):
    template_name='mypage/createOrUpdate.html'
    form_class = jobHunting_startTime_form
    model = jobHunting_startTime
    success_url = reverse_lazy('mypage:jobhunting_setting')
    def get_object(self):
        login_user=self.request.user
        try:
            start = jobHunting_startTime.objects.get(user=login_user)
        except:
            start  = jobHunting_startTime()
            start.user = login_user
        return start
    def get_context_data(self, **kwargs):
        context = super(jobHunting_startTime_view, self).get_context_data(**kwargs)
        context["h2text"]="就活開始時期を登録する"
        return context

class internshipRec_create(LoginRequiredMixin, generic.CreateView):
    model = internshipRecommendation
    form_class = internshipRec_form
    template_name="mypage/createOrUpdate.html"
    success_url=reverse_lazy('mypage:jobhunting_setting')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(internshipRec_create, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(internshipRec_create, self).get_context_data(**kwargs)
        context["h2text"]="おすすめのインターンシップ情報を追加する"
        return context

class prospectiveEmployer_create(LoginRequiredMixin, generic.CreateView):
    model = prospectiveEmployer
    form_class = prospectiveEmployer_form
    template_name="mypage/createOrUpdate.html"
    success_url=reverse_lazy('mypage:jobhunting_setting')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(prospectiveEmployer_create, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(prospectiveEmployer_create, self).get_context_data(**kwargs)
        context["h2text"]="内定した会社を追加する"
        return context

class internshipRec_update(LoginRequiredMixin, generic.UpdateView):
    model = internshipRecommendation
    form_class = internshipRec_form
    template_name="mypage/createOrUpdate.html"
    success_url=reverse_lazy('mypage:jobhunting_setting')
    def get_object(self):
        obj=internshipRecommendation.objects.get(auto_increment_id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(internshipRec_update, self).get_context_data(**kwargs)
        context["h2text"]="おすすめのインターンシップ情報を編集する"
        return context

class prospectiveEmployer_update(LoginRequiredMixin, generic.UpdateView):
    model = prospectiveEmployer
    form_class = prospectiveEmployer_form
    template_name="mypage/createOrUpdate.html"
    success_url=reverse_lazy('mypage:jobhunting_setting')
    def get_object(self):
        obj=prospectiveEmployer.objects.get(auto_increment_id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(prospectiveEmployer_update, self).get_context_data(**kwargs)
        print(kwargs)
        context["h2text"]="内定した会社を編集する"
        return context

class internshipRec_delete(LoginRequiredMixin, generic.DeleteView):
    model = internshipRecommendation
    success_url = reverse_lazy('mypage:jobhunting_setting')
    template_name = "mypage/confirmDel.html"
    def get_object(self):
        obj=internshipRecommendation.objects.get(auto_increment_id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(internshipRec_delete, self).get_context_data(**kwargs)
        print(kwargs)
        context["h2text"]="以下のインターンシップ情報を削除しますか"
        return context

class prospectiveEmployer_delete(LoginRequiredMixin, generic.DeleteView):
    model = prospectiveEmployer
    success_url = reverse_lazy('mypage:jobhunting_setting')
    template_name="mypage/confirmDel.html"
    def get_object(self):
        obj=prospectiveEmployer.objects.get(auto_increment_id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(prospectiveEmployer_delete, self).get_context_data(**kwargs)
        print(kwargs)
        context["h2text"]="以下の内定社情報を削除しますか"
        return context
