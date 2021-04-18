from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.email_template),
    path("email-sent/", views.email_sent),
]
