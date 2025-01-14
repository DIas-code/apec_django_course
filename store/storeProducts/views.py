from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'StoreApp',
        'username': 'Dias Yermekov',
        'is_promotion': False
    }
    return render(request, 'storeProducts/index.html', context)

def products(request):
    context = {
        'title': 'products'
    }
    return render(request, 'storeProducts/products.html', context)