#  coding:utf-8

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    meaasge = forms.CharField()