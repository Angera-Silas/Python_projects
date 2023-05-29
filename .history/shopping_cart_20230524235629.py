class Item():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    cart = []
    def __init__(self, Item,price):
        super().__init__(Item)
        self.price = price
    def add(self):
        tot
        self.cart.append(self.Item)
        