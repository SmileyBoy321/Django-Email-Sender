from django import forms
from django.forms.widgets import EmailInput, TextInput


class ComposeForm(forms.Form):
    email_to = forms.EmailField(label="To", widget=EmailInput)
    email_cc = forms.EmailField(label="CC", widget=EmailInput)
    email_subject = forms.CharField(
        required=False, widget=TextInput(attrs={"placeholder": "Subject"})
    )
    email_message = forms.CharField(required=True, label="", widget=forms.Textarea())
