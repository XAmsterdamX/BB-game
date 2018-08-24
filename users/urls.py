# users/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('instructor_request', views.instructor_request_view, name='instructor_request'),
    path('instructor_request_sent', views.instructor_request_sent_view, name='instructor_request_sent'),
]
