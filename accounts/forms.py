from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, PasswordChangeForm,
    PasswordResetForm, SetPasswordForm
)
from django.contrib.auth import get_user_model
from .models import (
    UserSetting
)

User = get_user_model()


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる





class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = ('email','last_name','first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_email(self):#clean_[フィールド名]のメゾットを定義するとそこで入力検証が行われる
        #もし重複するアクティブでない(仮登録だけして本登録をしないまま、登録フォームが期限切れしたなどした残骸を削除する)
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email
    """
    #正規表現を使って津田以外のメアドで登録しようとした人を弾くメソッドが必要
    def clean_email(self):
        emal = self.cleaned_data['email']
        if(!　　　[emailがtsuda.ac.jp]　　　): <--ここ直す
            raise forms.ValidationError("Allow @tsuda.ac.jp only.")
        return email
    """




COURSE_CHOICES=(
    ('1','英語英文学科'),
    ('2','国際関係学科'),
    ('3','多文化・国際協力学科'),
    ('4','数学科'),
    ('5','情報科学科'),
    ('6','総合政策学科'),
)
class UserSettingForm(forms.ModelForm):
    #メールアドレス認証後の設定form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['display_name'].required = False
        self.fields['icon_pic'].required = False
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserSetting
        fields = (
            'graduation_year',
            'course',
            'display_name',
            'icon_pic',
        )

class MyPasswordResetForm(PasswordResetForm):
    """パスワード忘れたときのフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MySetPasswordForm(SetPasswordForm):
    """パスワード再設定用フォーム(パスワード忘れて再設定)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
