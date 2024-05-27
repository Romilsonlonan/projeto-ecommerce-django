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
    if request.method == "POST":
        print(request.POST)
    return render(request, "contact/view.html", context)