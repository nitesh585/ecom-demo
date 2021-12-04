from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def categories(request):
    """return all categories present in database
    Returns: [dict]
    """
    return {"categories": Category.objects.all()}


def all_products(request):
    """renders home page and sends list of products
    present in database
    """
    products = Product.products.all()
    return render(request, "store/home.html", {"products": products})


def product_details(request, slug):
    """render product_details html with product of specific name"""
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, "store/products/product_details.html", {"product": product})


def category_details(request, slug):
    """render category_details html with category name and all the
    products present in this particular category
    """
    category = get_object_or_404(Category, slug=slug)
    products = Product.products.filter(category=category)
    return render(
        request,
        "store/products/category_details.html",
        {"category": category, "products": products},
    )
