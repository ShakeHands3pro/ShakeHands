from django.shortcuts import redirect,render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.forms import modelformset_factory
from .forms import(
    club_form, openQ_ans_addform, openQ_ans_updateform,
    jobHunting_startTime_form, jobHunting_requestment_form,
    internshipRec_form, prospectiveEmployer_form,
    myfriend_form, jobHunting_policy_form
)
from .models import(
    club, openQ_ans, openQ_ans,
    industry, occupation, prospectiveEmployer,
    jobHunting_startTime, jobHunting_requestment,
    internshipRecommendation,
    myfriend,jobHunting_policy
)
from accounts.models import(UserSetting,userComment)

# Create your views here.
class top(LoginRequiredMixin,generic.TemplateView):
    template_name = 'mypage/top.html'

User = get_user_model()


"""
大学生活情報登録・変更・削除
"""
class settingUnivLifeInfo(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mypage/UserSetting/UnivLifeInfo.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_user = self.request.user
        try:
            print(login_user.pk)
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
    template_name = 'mypage/confirmDel.html'
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
    template_name = 'mypage/confirmDel.html'
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
        except :
            req = None
        try:
            start = jobHunting_startTime.objects.get(user=login_user)
        except :
            start = None
        try:
            policy = jobHunting_policy.objects.get(user=login_user)
        except:
            policy = None
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
            'policy':policy,
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

class jobHuntingPolicy_view(LoginRequiredMixin, generic.UpdateView):
    template_name='mypage/createOrUpdate.html'
    form_class = jobHunting_policy_form
    model = jobHunting_policy
    success_url = reverse_lazy('mypage:jobhunting_setting')
    def get_object(self):
        login_user=self.request.user
        try:
            policy = jobHunting_policy.objects.get(user=login_user)
        except:
            policy  = jobHunting_policy()
            policy.user = login_user
        return policy
    def get_context_data(self, **kwargs):
        context = super(jobHuntingPolicy_view, self).get_context_data(**kwargs)
        context["h2text"]="就活の軸を追加する"
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
        obj=internshipRecommendation.objects.get(id=self.kwargs['id'])
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
        obj=prospectiveEmployer.objects.get(id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(prospectiveEmployer_update, self).get_context_data(**kwargs)
        context["h2text"]="内定した会社を編集する"
        return context

class internshipRec_delete(LoginRequiredMixin, generic.DeleteView):
    model = internshipRecommendation
    success_url = reverse_lazy('mypage:jobhunting_setting')
    template_name = "mypage/confirmDel.html"
    def get_object(self):
        obj=internshipRecommendation.objects.get(id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(internshipRec_delete, self).get_context_data(**kwargs)
        context["h2text"]="以下のインターンシップ情報を削除しますか"
        return context

class prospectiveEmployer_delete(LoginRequiredMixin, generic.DeleteView):
    model = prospectiveEmployer
    success_url = reverse_lazy('mypage:jobhunting_setting')
    template_name="mypage/confirmDel.html"
    def get_object(self):
        obj=prospectiveEmployer.objects.get(id=self.kwargs['id'])
        if obj.user==self.request.user:
            return obj
        raise Http404
        return None
    def get_context_data(self, **kwargs):
        context = super(prospectiveEmployer_delete, self).get_context_data(**kwargs)
        context["h2text"]="以下の内定社情報を削除しますか"
        return context






"""
プロフィールページを作成する
"""
class profilePage(LoginRequiredMixin, generic.TemplateView):
    template_name='mypage/profile.html'
    form_class= myfriend_form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        display_user = User.objects.get(id=self.kwargs['id'])

        #ユーザ情報を取得する
        try:
            userDetail = UserSetting.objects.get(user=display_user)
        except userDetail.DoesNotExist:
            UserDetail = None

        try:
            comment = userComment.objects.get(user=display_user)
        except userComment.DoesNotExist:
            comment = None
        
        #学生生活情報があれば取得する
        try:
            myClub = club.objects.filter(user=display_user)
        except club.DoesNotExist:
            myClub = None
        try:
            openQ_and_myans = openQ_ans.objects.filter(user=display_user)
        except openQ_ans.DoesNotExist:
            openQ_and_myans = None

        #就活情報があれば取得する
        try:
            req = jobHunting_requestment.objects.get(user=display_user)
        except :#jobHunting_requestment.models.DoesNotExist:
            req = None
        try:
            start = jobHunting_startTime.objects.get(user=display_user)
        except :#jobHunting_startTime.DoesNotExist:
            start = None
        try:
            policy = jobHunting_policy.objects.get(user=display_user)
        except:
            policy = None
        try:
            internshipRec = internshipRecommendation.objects.filter(user=display_user)
        except internshipRecommendation.DoesNotExist:
            internshipRec = None
        try:
            prospectiveEmp = prospectiveEmployer.objects.filter(user=display_user)
        except prospectiveEmployer.DoesNotExist:
            prospectiveEmp = None
        follow_state=get_friendState(self.request.user, display_user)
        context.update({
            'display_user':display_user,
            'userComment':comment,
            'display_name':get_display_name(display_user),
            'follow_state':follow_state,
            'followButton_txt':'フォロー解除' if follow_state <3 else 'フォロー' if follow_state<5 else '',
            'user_detail':userDetail,
            'club':myClub,
            'openQ':openQ_and_myans,
            'jobReqestment':req,
            'policy':policy,
            'jobHunting_startTime':start,
            'internship_rec':internshipRec,
            'prospective_employer':prospectiveEmp,
        })
        print(follow_state)
        return context
    def post(self, request, *args, **kwargs):
        followstate_changeParam = int(request.POST.get('followstate_ChangeParam',None))
        print("followstate_changeParamは"+str(followstate_changeParam))
        display_user = User.objects.get(id=self.kwargs['id'])
        if(followstate_changeParam <3):
            try:
                friend_model=myfriend.objects.get(user=self.request.user, friend=display_user)
            except myfriend.DoesNotExist:
                raise Http404
            friend_model.delete()
        elif(followstate_changeParam <5):
            data={
                'user':self.request.user.id,
                'friend':display_user.id
            }
            form = self.form_class(data=data)          
            if form.is_valid():
                form.save()
            else:
                print("save失敗")
        return redirect('mypage:profile',id=display_user.pk)

def get_display_name(user):
    try:
        displayname = UserSetting.objects.get(user=user).display_name
        return displayname
    except:
        return user.get_full_name()

def get_friendState(login_user,theOther):
    is_follow=myfriend.objects.filter(user=login_user, friend=theOther)
    is_followed=myfriend.objects.filter(user=theOther, friend=login_user)
    if(is_follow and is_followed):
        return 1#相互フォローしている
    elif(is_follow):
        return 2#フォローはしているけど、相手からはフォローされていない
    elif(is_followed):
        return 3#フォローされているけど、フォローしてない
    elif(login_user.pk==theOther.pk):
        return 5#本人
    else:
        return 4#他人


class allUser_list(LoginRequiredMixin, generic.TemplateView):
    template_name='mypage/userlist.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usersettings=UserSetting.objects.exclude(user=self.request.user)
        context.update({
            'users':usersettings,
        })
        print(context)      
        return context
    def get(self, request, *args, **kwargs):
        return super(allUser_list, self).get(request, *args, **kwargs)

        
