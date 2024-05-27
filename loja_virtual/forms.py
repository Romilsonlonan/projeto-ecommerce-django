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
    
    #def clean_email(self):
    #    if self.is_valid():
    #        email = self.cleaned_data['email']
    #        if not "gmail.com" in email:
    #            raise forms.ValidationError("O Email deve ser do gmail.com") 
    #        return email
    #    return None  # Ou retorne outro valor caso o formulário não seja válido

    
    