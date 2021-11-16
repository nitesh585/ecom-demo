class Basket:
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get("skey")
        if "skey" not in request.session:
            basket = self.session["skey"] = {}
        self.basket = basket

    def add(self, product, product_qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id not in self.basket:
            self.basket[product_id] = {
                "price": str(product.price),
                "qty": int(product_qty),
            }
        self.session.modified = True
