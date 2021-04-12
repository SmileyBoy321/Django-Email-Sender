from django import forms
from django.forms.widgets import EmailInput, TextInput


class ComposeForm(forms.Form):
    # Multiple email addresses to email_cc. Check the last answer in the link below.
    # https://stackoverflow.com/questions/12698474/django-form-validation-accepting-multiple-values-for-one-field
    email_to = forms.EmailField(label="To", widget=EmailInput(attrs={"size": 76}))
    email_cc = forms.EmailField(
        label="CC",
        required=False,
        widget=EmailInput(attrs={"size": 76, "multiple": True}),
    )
    email_subject = forms.CharField(
        required=False, widget=TextInput(attrs={"placeholder": "Subject", "size": 76})
    )
    email_message = forms.CharField(
        required=True, label="", widget=forms.Textarea(attrs={"rows": 19, "cols": 78})
    )
