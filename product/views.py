from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from product.models import Product,Category
# Create your views here.

def hello_view(request):
    return HttpResponse("Hi, it is my project")
def current_date_view(request):
    return HttpResponse(f"{datetime.now()}")
def goodbye_view(request):
    return HttpResponse("Bye Bye")
def main_view(request):
    return render(request, 'index.html')
def products_view1(request,id):
    if request.method == 'GET':
        try:
            category = Category.objects.get(id=id)
            products = Product.objects.filter(category=category)
        except :
            return HttpResponse("page not found")
        return render(request=request,
                      template_name='product/product_list.html',
                      context={'products': products})

def products_view2(request):
    if request.method == 'GET':
        products=Product.objects.all()
        return render(request=request,
                      template_name='product/product_list.html',
                      context={'products': products})
def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'product/category_list.html', context={'c': categories})


def product__detail_view(request,id=0,prid=0):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=prid)
        except Product.DoesNotExist:
            return HttpResponse("page not found")
        return render(request=request, template_name='product/product_detail.html', context={'p':product})