from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):

    username = forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Usuario',
                'autocomplete': 'off',
            }
        ))
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Contraseña',
                'autocomplete': 'off',
            }
        ))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError(
                'Usuario o Contraseña Incorrecta'
            )

        return self.cleaned_data
