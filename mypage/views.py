from django.shortcuts import render
from django.shortcuts import redirect,render
from django.template.loader import render_to_string
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class top(LoginRequiredMixin,generic.TemplateView):
    template_name = 'mypage/mypage.html'