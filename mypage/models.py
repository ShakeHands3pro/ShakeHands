from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from accounts.models import(
    User
)

"""以下UUIDを利用するための設定"""
import uuid
from json import JSONEncoder
from uuid import UUID
JSONEncoder_olddefault = JSONEncoder.default
def JSONEncoder_newdefault(self, o):
    if isinstance(o, UUID): return str(o)
    return JSONEncoder_olddefault(self, o)
JSONEncoder.default = JSONEncoder_newdefault



# Create your models here.
"""
＿＿＿＿＿＿＿＿就活関連のモデル＿＿＿＿＿＿＿＿＿
＊業界モデル
＊職種モデル
＊就活希望条件モデル
＊就活開始時期モデル
＊おすすめのインターンシップモデル
＊内定済の会社モデル
"""
class industry(models.Model):
    #業界[id,大分類,小分類]　
    auto_increment_id = models.AutoField(primary_key=True)
    industry_classification = models.CharField("業界分類",max_length=50)
    industry = models.CharField("業界",max_length=50,blank=True)
    def __str__(self):
        if(len(self.industry)==0):
            return str(self.industry_classification+" 業界")
        return str(self.industry_classification+" "+self.industry+" 業界")

class occupation(models.Model):
    #職種[id,職種]　
    auto_increment_id = models.AutoField(primary_key=True)
    occupation = models.CharField("職種", max_length=50)
    def __str__(self):
        return self.occupation

class jobHunting_requestment(models.Model):
    #就職希望[業界、職種、勤務地]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    industry = models.ForeignKey(industry, verbose_name='希望業界', on_delete=models.CASCADE)
    occupation = models.ForeignKey(occupation, verbose_name='希望職種', on_delete=models.CASCADE)
    workplace = models.CharField("希望勤務地", max_length=255, blank=True, null=True)

class jobHunting_startTime(models.Model):
    #就活を始めた時期[時期]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    season = models.CharField("時期", max_length=50, blank=False, null=True)
    def __str__(self):
        return self.season

class internshipRecommendation(models.Model):
    #インターン情報[業界、職種、社名、時期、期間、内容、感想、最終更新日、1対多の関係]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    industry = models.ForeignKey(industry, verbose_name='業界', on_delete=models.CASCADE, blank=True, null=True)
    occupation = models.ForeignKey(occupation, verbose_name='職種', on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.CharField("社名", max_length=50)
    season = models.CharField("時期", max_length=50)
    period = models.CharField("期間", max_length=50)
    overView = models.TextField("内容", max_length=500)
    implessions = models.TextField("感想", max_length=300,blank=True, null=True)
    post_date = models.DateTimeField("最終更新日", auto_now= True)

class prospectiveEmployer(models.Model):
    #内定済みの会社[業界、職種、社名、1対多の関係]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    industry = models.ForeignKey(industry, verbose_name='業界', on_delete=models.CASCADE)
    occupation = models.ForeignKey(occupation, verbose_name='職種', on_delete=models.CASCADE)
    company_name = models.CharField("社名", max_length=50)







"""
______________友達＿＿＿＿＿＿＿＿＿＿＿
＊友達モデル
"""
class myfriend(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete = models.CASCADE, related_name='friend')







"""
______________学生生活＿＿＿＿＿＿＿＿＿＿＿
＊所属団体モデル
＊OpenQuestionモデル
＊OpenQuestion回答モデル
"""
class club(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    implessions = models.CharField("団体名", max_length=60,blank=True)
    post_date = models.DateTimeField("最終更新日", auto_now= True)

class openQ(models.Model):
    q_text = models.TextField("Q")
    def __str__(self):
        return self.q_text

class openQ_ans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    openQ = models.ForeignKey(openQ, on_delete=models.PROTECT)
    post_date = models.DateTimeField("最終更新日", auto_now= True)