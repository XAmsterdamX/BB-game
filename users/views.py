# users/views.py

from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, InstructorRequestForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def instructor_request_view(request):
    if request.method == 'GET':
        form = InstructorRequestForm()
    else:
        form = InstructorRequestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_first_name'] + ' ' + form.cleaned_data['your_surname']
            subject = 'Instructor access request from ' + name
            sender = form.cleaned_data['your_email']
            message_line_1 = name + ' is requesting instructor access to Battle of the Brewers <br/><br/>'
            message_line_2 = 'Username: ' + form.cleaned_data['your_organization'] + '<br/>'
            message_line_3 = 'Organization: ' + form.cleaned_data['your_organization'] + '<br/>'
            message_line_4 = 'Email:: ' + form.cleaned_data['your_email']
            message_line_5 = '<br/><br/>BB'
            message = message_line_1 + message_line_2 + message_line_3 + message_line_4 + message_line_5
            recipient = ['ecjboon@gmail.com']
            try:
                msg = EmailMessage(subject, message, sender, recipient)
                msg.content_subtype = 'html'
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('instructor_request_sent')
    return render(request, 'instructor_request.html', {'form': form})


def instructor_request_sent_view(request):
    return render(request, 'instructor_request_sent.html')





