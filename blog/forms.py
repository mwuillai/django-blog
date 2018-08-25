from django import forms
from django.contrib.auth.models import User

class ConnectionForm(forms.Form):
    username = forms.CharField(label='Utilisateur', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='mot de passe', required=True)