from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import ComposeForm


def email_template(request):
    if request.method == "GET":
        form = ComposeForm()
    else:
        form = ComposeForm(request.POST)
        if form.is_valid():
            print(form)
            email_to = form.cleaned_data["email_to"]
            email_cc = form.cleaned_data["email_cc"]
            email_subject = form.cleaned_data["email_subject"]
            email_message = form.cleaned_data["email_message"]

            print("DEBUG:", email_to)
        else:
            print("DEBUG:", form.errors)
    return render(request, "email_template.html", {"form": form})
