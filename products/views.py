from typing import Any
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Product 

class ProductListView(ListView):
    
    # Traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all() 
    template_name = "products/list.html"
    
#    def get_context_data(self, *args, **kwargs):
#        context = super(ProductListView, self).get_context_data(*args, **kwargs)
#        print (context)
#        return context
    
# Função Based View    
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs': queryset
    }
    return render(request, "products/list.html", context)


# Função Based View
class ProductDetailView(DetailView):
    
    # Traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all()
    template_name = "products/detail.html"    
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print (context)
        return context
    
# Função Based View    
def product_detail_view(request, pk=None, *args, **kwargs):
    
    #instance = Product.objects.get(pk=pk)
    instance = get_object_or_404(Product, pk=pk)
    queryset = Product.objects.all()
    context = {
        'object_list': instance
    }
    return render(request, "products/detail.html", context)
