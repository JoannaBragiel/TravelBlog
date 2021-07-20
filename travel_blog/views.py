from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'home_page.html'