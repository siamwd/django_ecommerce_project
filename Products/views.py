from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product

def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    context ={
        'categories':categories,
        'products':products
    }

    return render(request, 'product/products.html',context)
# Create your views here.
def category_product_list(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(
        available=True,
        category=category
    )
    categories = Category.objects.all()

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, 'product/products.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'product/product_details.html', {'product':product})