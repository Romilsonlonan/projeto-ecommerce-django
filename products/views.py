from django.shortcuts import render
from django.views.generic import ListView
from .models import Product 

class ProductListView(ListView):
    
    # Traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all() 
    
# Função Based View    
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs': queryset
    }
    return render(request, "products/list.html", context)
