from django.contrib import admin
from .models import(
    QIndex
)

# Register your models here.
class QIndexAdmin(admin.ModelAdmin):
    fields = ['index']

admin.site.register(QIndex,QIndexAdmin)