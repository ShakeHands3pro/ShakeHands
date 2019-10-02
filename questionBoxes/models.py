from django.db import models
from django.utils import timezone

# Create your models here.
import uuid
from json import JSONEncoder
from uuid import UUID
from accounts.models import (
    User
)

JSONEncoder_olddefault = JSONEncoder.default

def JSONEncoder_newdefault(self, o):
    if isinstance(o, UUID): return str(o)
    return JSONEncoder_olddefault(self, o)

JSONEncoder.default = JSONEncoder_newdefault

STATE_CHOICES=(
    ('1','回答待ち'),
    ('2','回答済'),
    ('3','非表示'),
)

class QIndex(models.Model):
    """質問タグ"""
    index = models.CharField(max_length=32)
    def __str__(self):
        return self.index


class Question(models.Model):
    """ 質問 """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    questionner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requester')
    answerer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='replyer')
    question = models.TextField("質問",blank=False, null=False)
    created_at = models.DateTimeField("作成日",default=timezone.now)
    status = models.CharField("ステータス",max_length=1,choices=STATE_CHOICES,blank=False,default=1)
    index = models.ManyToManyField(QIndex)
    def __str__(self):
        return self.question

""" class Answer(models.Model):
    回答
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='question')
    advice = models.TextField("回答",blank=False, null=False)
    created_at = models.DateTimeField("回答日",default=timezone.now)
    def __str__(self):
        return self.answer """


""" class Like(models.Model):
    いいね機能
   answer =models.ForeignKey(Answer, on_delate=models.CASCADE, related_name='like_answer')
   user =models.ForeignKey(User,on_delate=models.CASCADE) """
  
