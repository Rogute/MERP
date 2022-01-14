from django import forms
from .models import Event


class RegisterForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.all(), label="Event")
    name = forms.CharField(label="Name")
    surname = forms.CharField(label="Surname")
    e_mail = forms.EmailField(label="E-mail")