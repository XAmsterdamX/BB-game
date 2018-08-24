# game/views.py

from django.views.generic import TemplateView
from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class InstructionsPageView(TemplateView):
    template_name = 'instructions.html'










