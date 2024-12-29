class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart

    def add_product(self, product, quantity):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                "product_id": product_id,
                "name": product.name,
                "price": str(product.price),
                "quantity": 0,
                "image": product.image.url,
                "category": product.category.name,
                "total_amount": "0"
            }
        self.cart[product_id]["quantity"] += quantity
        self.cart[product_id]["total_amount"] = f"{product.price * self.cart[product_id]['quantity']:,.2f}"
        self.save()

    def save(self):
        self.session.modified = True

    def get_total_amount(self):
        total_amount =  sum(float(product["price"]) * product["quantity"]
                            for product in self.cart.values())

        formatted_total_amount = f"{total_amount:,.2f}"

        return formatted_total_amount

    def remove_product(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session["cart"]
        self.save()
