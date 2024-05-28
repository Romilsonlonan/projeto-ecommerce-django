from django import forms 
from django.contrib.auth import get_user_model

User = get_user_model()
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
        error_messages={'invalid': 'Digite um e-mail válido!'},

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
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com") 
        return email 
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Esse usuario ja existe, escolha outro nome!")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Esse email já existe, tente outro!")
        return email
    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("As senhas informadas tem que ser iguais!")
        return data
            

    
    