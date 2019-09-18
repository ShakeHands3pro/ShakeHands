from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import (
    club, openQ_ans, openQ,
    industry, occupation, prospectiveEmployer,
    jobHunting_startTime, jobHunting_requestment,
    internshipRecommendation
)

# Register your models here.
class clubAdmin(admin.ModelAdmin):
    fields = ['club_name']
class openQAdmin (admin.ModelAdmin):
    fields = ['q_text']
class openQ_ansAdmin(admin.ModelAdmin):
    fields = ['user','openQ','ans']

class industryAdmin(admin.ModelAdmin):
    fields = ['industry_classification', 'industry']
class occupationAdmin(admin.ModelAdmin):
    fields = ['occupation']
class prospectiveEmployerAdmin(admin.ModelAdmin):
    fields = ['industry', 'occupation', 'company_name']
class jobHunting_requestmentAdmin(admin.ModelAdmin):
    fields = ['industry','occupation','workplace']
class jobHunting_startTimeAdmin(admin.ModelAdmin):
    fields = ['season']



admin.site.register(club,clubAdmin)
admin.site.register(openQ,openQAdmin)
admin.site.register(openQ_ans,openQ_ansAdmin)
admin.site.register(industry, industryAdmin)
admin.site.register(occupation, occupationAdmin)
admin.site.register(prospectiveEmployer, prospectiveEmployerAdmin)
admin.site.register(jobHunting_requestment, jobHunting_requestmentAdmin)
admin.site.register(jobHunting_startTime,jobHunting_startTimeAdmin)