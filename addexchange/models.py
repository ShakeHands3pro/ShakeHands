from django.db import models
from accounts.models import (
    User
)
from django.utils import timezone
import datetime
import uuid
from json import JSONEncoder
from uuid import UUID

JSONEncoder_olddefault = JSONEncoder.default

def JSONEncoder_newdefault(self, o):
    if isinstance(o, UUID): return str(o)
    return JSONEncoder_olddefault(self, o)

JSONEncoder.default = JSONEncoder_newdefault



class addressExchange(models.Model): #連絡先交換クラス
    #id
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    #editableは「編集可能かどうか」

    #質問者　Userモデル
    questioner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='questioner')
    

    #回答者　Userモデル
    answerer=models.ForeignKey(User, on_delete=models.CASCADE, related_name='answerer')
   

    #メアド交換申請目的
    text=models.TextField(
        verbose_name='交換申請目的',
        blank=False,
        null=False,
        max_length=400,
    )

    #承認 intかBooleanか確認した方がいい
    approve_boolean=models.BooleanField(
    verbose_name='承認',
    blank=True,
    null=True,

    )
    #申請日時
    request_time=models.DateTimeField(
        verbose_name='申請日時',blank=False,null=False,default=timezone.now)

    #承認日時
    accepted_time=models.DateTimeField(
        verbose_name='承認日時',blank=True,null=True)
 
    def __str__(self):
        return self.text