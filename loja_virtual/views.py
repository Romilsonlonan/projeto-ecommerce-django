from django import forms
from django.http import HttpResponse
from django.shortcuts import render 
from .forms import ContactForm

def home_page(request):
    context = {
        "title": "Pagina principal",
        "content": "Seja Bem a Pagina principal"
    }
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