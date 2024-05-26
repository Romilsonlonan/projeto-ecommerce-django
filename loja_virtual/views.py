from django.http import HttpResponse
from django.shortcuts import render 

def home_page(request):
    context = {
        "title": "Pagina principal"
        "content" "Seja Bem a Pagina principal"
    }
    return render(request, "home_page.html", context)