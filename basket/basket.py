class Basket:
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary
    """

    def __init__(self, request) -> None:
        self.session = request.session
        basket = self.session.get("skey")
        if "skey" not in self.session:
            basket = self.session["skey"] = {'number':4518}
        self.basket = basket
