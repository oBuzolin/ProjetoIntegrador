# users/forms.py
from django import forms

class LoginForm(forms.Form):
    usuario = forms.EmailField(max_length=255)
    senha = forms.CharField(widget=forms.PasswordInput)


class PasswordResetForm(forms.Form):
    usuario = forms.CharField(
        label='Usuário', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário', 'id': 'validationCustom01',})
    )
    nova_senha = forms.CharField(
        label='Nova Senha', 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nova Senha', 'id': 'nova_senha' })
    )
    confirmar_senha = forms.CharField(
        label='Confirme a Nova Senha', 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a Nova Senha', 'id': 'confirmar_senha' })
    )

    def clean(self):
        cleaned_data = super().clean()
        nova_senha = cleaned_data.get("nova_senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if nova_senha and confirmar_senha:
            if nova_senha != confirmar_senha:
                raise forms.ValidationError("As senhas não coincidem.")
            elif len(nova_senha) < 8 and len(confirmar_senha) < 8:
                    raise forms.ValidationError("A senha precisa ter no mínimo 8 caracteres")
