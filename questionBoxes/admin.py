from django.contrib import admin
from .models import(
    QIndex,Question,Answer,Like
)


# Register your models here.
class QIndexAdmin(admin.ModelAdmin):
    fields = ['index']
class QuestionAdmin(admin.ModelAdmin):
    fields=['title','questionner','answerer','text','status','index']
class AnswerAdmin(admin.ModelAdmin):
    fields=['question','advice']
class LikeAdmin(admin.ModelAdmin):
    fields=['user','answer']

admin.site.register(QIndex,QIndexAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Like, LikeAdmin)