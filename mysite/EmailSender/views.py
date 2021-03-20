from django import template
from django.shortcuts import render


def index(request):
        return render(request, "EmailSender/index.html")
