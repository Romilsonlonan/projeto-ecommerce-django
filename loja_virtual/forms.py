from django import forms 

class ContactForm(forms.Form):
    nome_completo = forms.CharField(
        error_messages={'required': 'Obrigatório o preechimento do nome'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder":"Digite seu nome completo"
            }
        )
    )
    email = forms.EmailField(
        error_messages={'required': 'Digite um e-mail válido'},

        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                "placeholder":"Digite seu e-mail"
            }
        )
    )
    content = forms.CharField(
        error_messages={'required': 'Digite a sua mensagem'},

        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                "placeholder":"Digite sua mensagem"
            }
        )
    )