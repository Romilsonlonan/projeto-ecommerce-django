from django.http import HttpResponse
from django.shortcuts import render 

def home_page(request):
    context = {
        "title": "Pagina principal"
        "content" "Seja Bem a Pagina principal"
    }
    return render(request, "home_page.html", context) 

def about_page(request):
    context = {
        "title": "Pagina sobre"
        "content" "Seja Bem a Pagina sobre"
    }
    return render(request, "about_page.html", context)

def contact_page(request):
    context = {
        "title": "Pagina de contatos"
        "content" "Seja Bem a Pagina de contatos"
    }
    return render(request, "contact_page.html", context)