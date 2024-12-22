from django.shortcuts import render
from . models import producte
from django.core.paginator import Paginator
from django.contrib.auth import authenticate

 

# Create your views here.
def index(request):
    
    obj=producte.objects.all() 
    list_data={'obj':obj}
    return render(request,'index.html',list_data)

def list_producte(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    obj=producte.objects.all()
    producte_paginator=Paginator(obj,8)
    obj=producte_paginator.get_page(page)
    list_data={'obj':obj,'page':producte_paginator}

    

    return render(request,'product.html',list_data)

def detail_product(request,id):
    obj=producte.objects.get(id=id)
    list_data={'obj':obj}
    return render(request,'product-detail.html',list_data)


