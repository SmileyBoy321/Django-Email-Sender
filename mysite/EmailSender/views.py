from django import template
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
        return render(request, "EmailSender/index.html")

def compose(request):
        return render(request, "EmailSender/email_template.html")
