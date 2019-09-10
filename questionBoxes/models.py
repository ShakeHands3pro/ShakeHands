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
class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    questionner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questionner')
    answerer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='answerer')
    question = models.TextField("質問",blank=False, null=False)
    created_at = models.DateTimeField("作成日",default=timezone.now)
    status = models.CharField("ステータス",max_length=1,choices=STATE_CHOICES,blank=False)
    def __str__(self):
        return question
