from django import forms

#  from django.forms.fields import MultiValueField
from django.forms.widgets import EmailInput, TextInput


class ComposeForm(forms.Form):
    email_to = forms.EmailField(
        label="To", widget=EmailInput(attrs={"size": 76, "class": "form-control"})
    )
    email_cc = forms.EmailField(
        label="CC",
        required=False,
        widget=EmailInput(attrs={"size": 76, "class": "form-control"}),
    )
    email_subject = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={"placeholder": "Subject", "size": 76, "class": "form-control"}
        ),
    )
    email_message = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 19,
                "cols": 78,
                "class": "form-control",
                "style": "resize: none",
            }
        ),
    )
