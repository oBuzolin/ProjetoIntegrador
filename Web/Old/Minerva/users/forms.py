# users/forms.py
from django import forms

class LoginForm(forms.Form):
    usuario = forms.EmailField(max_length=255)
    senha = forms.CharField(widget=forms.PasswordInput)
