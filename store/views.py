from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def categories(request):
    return {"categories": Category.objects.all()}


def all_products(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, "store/products/product_details.html", {"product": product})


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "store/products/category_details.html",
        {"category": category, "products": products},
    )
