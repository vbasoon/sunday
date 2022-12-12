from django.shortcuts import render

from .models import SalesOrder
# from ..products.models import Product


# Create your views here.
def orders_page(request):
    orders = SalesOrder.objects.all()
    #products = Product.objects.all()
    context = {
        'orders': orders,
        #'products': products
    }
    return render(request, 'index.html', context)
