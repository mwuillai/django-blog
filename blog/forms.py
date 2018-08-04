from django import forms


class Inscription(forms.Form):
    Login = forms.CharField(
        label='Identifiant',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )