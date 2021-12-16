from django.shortcuts import get_object_or_404, render

from .models import Category, Product
from account.models import UserBase
import random
from datetime import date


def bulkInsert():
    """method deletes all the categories and products form DB
    and adds new categories and products according to configuration
    """
    Category.objects.all().delete()
    Product.products.all().delete()
    i = 1
    category = [
        "Category_1",
        "Category_2",
        "Category_3",
        "Category_4",
        "Category_5",
        "Category_6",
        "Category_7",
        "Category_8",
        "Category_9",
        "Category_10",
    ]
    images = [
        "one.png",
        "two.jpg",
        "three.png",
        "four.png",
        "five.jpg",
        "six.jpeg",
        "seven.jpg",
        "eight.jpg",
        "nine.jpg",
        "ten.jpg",
    ]
    j = 1
    category_obj = []
    for cat in category:
        form = Category(name=cat, slug=cat)
        form.pk = j
        category_obj.append(form)
        form.save()
        j += 1

    for i in range(100):
        idx = random.randint(0, 9)
        idx2 = random.randint(0, 9)

        descript = "Machine learning (ML) is the study of \
                computer algorithms that can improve automatically\
                through experience and by the use of data.[1] It\
                is seen as a part of artificial intelligence. Machine \
                learning algorithms build a model based on sample data,\
                known as training data, in order to make predictions\
                or decisions without being explicitly programmed to\
                do so.[2] Machine learning algorithms are used in a wide variety\
                of applications, such as in medicine, email filtering,\
                speech recognition, and computer vision, where it is \
                difficult or unfeasible to develop conventional algorithms\
                to perform the needed tasks.[3] ".split()
        random.shuffle(descript)
        descript = " ".join(descript)

        userbase = UserBase.objects.all()
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        prc = random.random() * 100
        pd = Product(
            category=category_obj[idx],
            created_by=userbase[0],
            title=str("Long Title_" + str(i)),
            description=descript,
            image=images[idx2],
            slug=str(i),
            price=prc,
            created=date(2021, month, day),
        )
        pd.pk = i
        pd.save()
        i += 1


def categories(request):
    """return all categories present in database
    Returns: [dict]
    """
    # bulkInsert()
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
