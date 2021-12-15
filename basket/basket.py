from decimal import Decimal

from store.models import Product


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

        if product_id in self.basket:
            self.basket[product_id]["qty"] = int(product_qty)
        else:
            self.basket[product_id] = {
                "price": str(product.price),
                "qty": int(product_qty),
            }
        self.save()

    def get_total_price(self):
        """
        get total price of product after multiplying
        quantity with price.
        """
        return sum(
            Decimal(item["price"]) * item["qty"] for item in self.basket.values()
        )

    def delete(self, product_id):
        """
        Delete item from session data
        """
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def update(self, product_id, product_qty):
        """
        Update qty from session data
        """

        if product_id in self.basket:
            self.basket[product_id]["qty"] = int(product_qty)

            basket = self.basket.copy()
            item_price = Decimal(basket[product_id]["price"]) * int(product_qty)
            self.save()
            return str(item_price)

    def __len__(self):
        """
        get the basket data and count the qty of items
        """
        return sum(item["qty"] for item in self.basket.values())

    def __iter__(self):
        """
        Collect the product_ids in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def save(self):
        """
        let session object notify that something is modified
        in session data so that it can save data.
        """
        self.session.modified = True

    def clear(self):
        del self.session["skey"]
        self.save()
