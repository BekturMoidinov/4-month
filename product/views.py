from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from product.models import Product
# Create your views here.

def hello_view(request):
    return HttpResponse("Hi, it is my project")
def current_date_view(request):
    return HttpResponse(f"{datetime.now()}")
def goodbye_view(request):
    return HttpResponse("Bye Bye")
def main_view(request):
    return render(request, 'index.html')
def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request=request,
                      template_name='product/product_list.html',
                      context={'products': products})
