from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from store.models import Product
from basket.basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, "store/basket/summary.html", {"basket": basket})


def basket_add(request):
    basket = Basket(request)

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        product = get_object_or_404(Product, id=product_id)

        basket.add(product=product, product_qty=product_qty)
        basket_qty = basket.__len__()

        response = JsonResponse({"qty": basket_qty})
        return response


def basket_delete(request):
    basket = Basket(request)

    if request.POST.get("action") == "post":
        product_id = request.POST.get("productid")
        basket.delete(product_id=product_id)

        response = JsonResponse(
            {
                "success": True,
                "total_price": basket.get_total_price(),
                "qty": basket.__len__(),
            }
        )
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = request.POST.get("productid")
        product_qty = request.POST.get("productqty")

        item_price = str(basket.update(product_id=product_id, product_qty=product_qty))
        print(type(item_price), item_price)

        response = JsonResponse(
            {
                "success": True,
                "item_price": item_price,
                "total_price": str(basket.get_total_price()),
                "qty": basket.__len__(),
            }
        )
        print(response)
        return response
