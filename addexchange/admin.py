from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import (
    addressExchange
)
class addEchangeAdmin(admin.ModelAdmin):
    fields = ['questioner','answerer','text','approve_boolean','request_time','accepted_time']

admin.site.register(addressExchange,addEchangeAdmin)