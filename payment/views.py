import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from basket.basket import Basket
from orders.views import payment_confirmation


@login_required
def BasketView(request):
    basket = Basket(request)

    total_price = str(basket.get_total_price())
    total_price = total_price.replace(".", " ")
    total_price = int(total_price)
    total_price = 100
    print(total_price)
    stripe.api_key = "sk_test_51K5kkkSJJe1bpxbm2639DnadJVGm4fbnov7cPqDle873lNeIkGMsB9Q6JlfTSli0NgJOWZx1J0SeDIB6yn7juLng00ZdUNXnoa"
    intent = stripe.PaymentIntent.create(
        amount=total_price,
        currency="INR",
        metadata={"userid": request.user.id},
    )

    return render(request, "payment/home.html", {"client_secret": intent.client_secret})


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, "payment/orderplaced.html")


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == "payment_intent.succeeded":
        payment_confirmation(event.data.object.client_secret)

    else:
        print("Unhandled event type {}".format(event.type))

    return HttpResponse(status=200)
