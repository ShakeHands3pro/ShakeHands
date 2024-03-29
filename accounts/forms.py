from django import forms
from django.core import validators
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, PasswordChangeForm,
    PasswordResetForm, SetPasswordForm
)
from django.contrib.auth import get_user_model
from .models import (
    UserSetting,userComment
)
from PIL import Image
from django.core.files import File


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
        if not(email.endswith('@gm.tsuda.ac.jp')):
            raise forms.ValidationError("@tsuda.ac.jpのメールアドレスを指定してください。")
        return email




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
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = UserSetting
        fields = (
            'graduation_year',
            'course',
            'display_name',
        )
    def clean_graduation_year(self):
        graduation_year = self.cleaned_data['graduation_year']
        if(int(graduation_year)>=100):
            raise forms.ValidationError('卒業年度は西暦の下二桁を入力してください。')
        return graduation_year

    




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

class iconChangeForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = UserSetting
        fields = ('icon_pic','x','y','width','height',)

    def save(self):
        icon = super(iconChangeForm,self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        r = w if (w<=h) else h

        image = Image.open(icon.icon_pic)
        RectImage = image.crop((x,y,(r+x),(r+y)))
        resizedImage = RectImage.resize((300,300),Image.ANTIALIAS)
        resizedImage.save(icon.icon_pic.path)

        return icon

class comment_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(comment_form, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = userComment
        fields = (
            'comment',
        )