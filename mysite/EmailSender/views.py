from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import ComposeForm


def email_template(request):
    form = ComposeForm()
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "email_template.html", {"form": form})
