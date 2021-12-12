from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe
from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total_price = str(basket.get_total_price())
    total_price = total_price.replace(".", " ")
    total_price = int(total_price)
    total_price = 10
    print(total_price)
    stripe.api_key = "sk_test_51K5kkkSJJe1bpxbm2639DnadJVGm4fbnov7cPqDle873lNeIkGMsB9Q6JlfTSli0NgJOWZx1J0SeDIB6yn7juLng00ZdUNXnoa"
    intent = stripe.PaymentIntent.create(
        amount=total_price, currency="gbp", metadata={"userid": request.user.id}
    )

    return render(request, "payment/home.html", {"client_secret": intent.client_secret})
