from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .forms import ContactForm, LoginForm, RegisterForm, User 
from django.contrib.auth import authenticate, login, get_user_model

def home_page(request):
    context = {
        "title": "Pagina principal",
        "content": "Seja Bem a Pagina principal"
    }
    if request.user.is_authenticated():
        context["premium_content"] = "Você é um usuário Premium!"
    return render(request, "home_page.html", context) 

####################### PAGINA SOBRE #######################

def about_page(request):
    context = {
        "title": "Pagina sobre",
        "content": "Seja Bem a Pagina sobre"
    }
    return render(request, "about/view.html", context)


####################### PAGINA DE CONTATOS #######################

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Pagina de contatos",
        "content": "Seja Bem a Pagina de contatos",
        "form": contact_form
    } 
        
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    
    #if request.method == "POST":
    #    print(request.POST)
    #    print(request.POST.get('Nome_Completo'))
    #    print(request.POST.get('Email'))
    #    print(request.POST.get('Content'))
    return render(request, "contact/view.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
    }
    
    print("User logged in")
    #print(request.user.is_authenticated)
    
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print (user)
        #print(request.user.is_authenticated)
    
    if user is not None:
        #print(request.user.is_authenticated)
        login(request, user)
        print("Login Válido!")
        # redirecionar para uma pagina de sucesso
        return redirect("/")
    else:
        #Retorna uma mensagem de erro de 'login invelido'
        print("Login inválido")
    return render(request, "auth/login.html", context)     

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }
    
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print (new_user)
    return render(request, "auth/register.html", {})    


