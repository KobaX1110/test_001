from django.shortcuts import render
from django.views.generic import TemplateView


class Homeview(TemplateView):
    template_name = "user/index.html"
