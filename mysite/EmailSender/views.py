from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ComposeForm


def email_sent(request):
    return render(request, "email_sent.html")


def email_template(request):
    if request.method == "GET":
        form = ComposeForm()
    else:
        form = ComposeForm(request.POST)
        if form.is_valid():
            email_to = form.cleaned_data["email_to"]
            email_cc = form.cleaned_data["email_cc"]
            email_subject = form.cleaned_data["email_subject"]
            email_message = form.cleaned_data["email_message"]
            mail = send_mail(
                email_subject,
                email_message,
                "django@example.com",
                [email_to],
                fail_silently=False,
            )
            if mail:
                return HttpResponseRedirect("email-sent/")

    return render(request, "email_template.html", {"form": form})
