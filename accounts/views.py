from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordChangeDoneView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect,render
from django.template.loader import render_to_string
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm,UserSettingForm,
    MyPasswordResetForm, MySetPasswordForm,iconChangeForm
)
from .models import (
    UserSetting
)

#デフォルトかカスタムか、そのプロジェクトで使用しているUserモデルが取得される。
User = get_user_model()

"""
class Top(generic.TemplateView):
    template_name = 'accounts/top.html'
"""

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('mypage:top')
        else:
            return super().post(request, *args, **kwargs)

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/logout.html'





class UserCreate(generic.CreateView):
    """ユーザー仮登録"""
    template_name = 'accounts/signup.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        """仮登録と本登録用メールの発行."""
        # 仮登録と本登録の切り替えは、is_active属性を使うと簡単です。
        # 退会処理も、is_activeをFalseにするだけにしておくと捗ります。
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # アクティベーションURLの送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('accounts/mail_template/signup/subject.txt', context).replace("\n","")
        message = render_to_string('accounts/mail_template/signup/message.txt', context)

        user.email_user(subject, message)
        return redirect('accounts:signup_done')


class UserCreateDone(generic.TemplateView):
    """ユーザー仮登録したよ"""
    template_name = 'accounts/signup_done.html'


class UserCreatesetting(generic.View):
    """メール内URLアクセス後のユーザー本登録"""
    template_name = 'accounts/signup_setting.html'
    form_class = UserSettingForm
    model = UserSetting
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内



    def get(self, request, **kwargs):
        return render(request,self.template_name,{'form':self.form_class})


    def post(self,request,**kwargs):
        """tokenが正しければ本登録."""
        form = self.form_class(request.POST)
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest("期限切れ")

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:#これに引っかかるはず
                    user.is_active = True
                    user.save()
                    getform=form.save(commit=False)
                    getform.user=user
                    getform.save()
                    return redirect('accounts:signup_complete')
        return HttpResponseBadRequest()


class UserCreateComplete(LoginRequiredMixin,generic.TemplateView):
    """ユーザー本登録したよ"""
    template_name = 'accounts/signup_complete.html'

class UserSettingUpdate(LoginRequiredMixin,generic.UpdateView):
    template_name = 'accounts/signup_setting.html'
    form_class = UserSettingForm
    model = UserSetting
    success_url = reverse_lazy('mypage:top')
    def get_object(self):
        obj=UserSetting.objects.get(user=self.request.user)
        return obj
    

class iconPic_change(LoginRequiredMixin,generic.TemplateView):
    template_name = 'accounts/set_iconpic.html'
    form = iconChangeForm
    def get_object(self):
        obj = UserSetting.objects.get(user=self.request.user)
        return obj
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        settings = UserSetting.objects.get(user=self.request.user)
        if settings.icon_pic:
            context.update({
                'icon_now':settings.icon_pic,
            })
        return context
<<<<<<< HEAD
=======
    def post(self,request):
        model = UserSetting.objects.get(user=self.request.user)
        form = iconChangeForm(request.POST,request.FILES,instance=model)
        if form.is_valid():
            form.save()
        return redirect('accounts:iconSetting')
    def get(self, request, **kwargs):
        settings = UserSetting.objects.get(user=self.request.user)
        if settings.icon_pic:
            return render(request,self.template_name,{'form':self.form,'icon_now':settings.icon_pic})
        return render(request,self.template_name,{'form':self.form})

>>>>>>> origin/master



"""**********************************************************
パスワード再設定について
"""

class PasswordReset(PasswordResetView):
    """パスワード変更用URLの送付ページ"""
    subject_template_name = 'accounts/mail_template/password_reset/subject.txt'
    email_template_name = 'accounts/mail_template/password_reset/message.txt'
    template_name = 'accounts/password_reset_form.html'
    form_class = MyPasswordResetForm
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    """パスワード変更用URLを送りましたページ"""
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    form_class = MySetPasswordForm
    success_url = reverse_lazy('accounts:password_reset_complete')
    template_name = 'accounts/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'accounts/password_reset_complete.html'