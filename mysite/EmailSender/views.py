from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import NameForm

def thanks(request):
    return render(request, "thanks.html")

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("thanks/")
    else:
        form = NameForm()

    return render(request, "email_template.html", {"form": form})
