from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from django.views.generic import DetailView, CreateView, ListView

from product.models import Product, Category, Review
from product.forms import ProductForm, CategoryForm,ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.




@login_required(login_url='login')
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/product_list.html'

    # context = {'object_list': Post.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Category.objects.all()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )
        return queryset
@login_required(login_url='login')
class CategoryListView(ListView):
    model = Category
    context_object_name = 'name'
    template_name = 'product/category_list.html'

@login_required(login_url='/login/')
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'product/product_detail.html'
    pk_url_kwarg = 'prid'
    success_url = '/products/'
@login_required(login_url='login')
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product_detail.html'
    pk_url_kwarg = 'prid'

@login_required(login_url='login')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_product_form.html'
    success_url = '/products/'

@login_required(login_url='/login')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/create_category_form.html'
    success_url = '/products/'

