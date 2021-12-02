from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from basket.basket import Basket
from store.models import Product


def basket_summary(request):
    """method used to load summary page of
    current basket.

    Args:
        request ([object])

    Returns: renders summary html page and send basket to it
    """
    basket = Basket(request)
    return render(request, "store/basket/summary.html", {"basket": basket})


def basket_add(request):
    """method used to all product to basket

    Args:
        request ([object])

    Returns:
        [JsonResponse]: returns number of products in basket
    """
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
    """method used to remove product from basket

    Args:
        request ([object])

    Returns:
        [JsonResponse]: returns total price and total number of
                        products present in basket.
    """
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
    """method responsible for updating the basket

    Args:
        request ([object])

    Returns:
        [JsonResponse]: returns updated item price of product and
                        total price and quantity of basket.
    """
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = request.POST.get("productid")
        product_qty = request.POST.get("productqty")

        item_price = str(basket.update(product_id=product_id, product_qty=product_qty))
        # print(type(item_price), item_price)

        response = JsonResponse(
            {
                "success": True,
                "item_price": item_price,
                "total_price": str(basket.get_total_price()),
                "qty": basket.__len__(),
            }
        )
        # print(response)
        return response
