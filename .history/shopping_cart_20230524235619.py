class Item():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    cart = []
    tot
    def __init__(self, Item,price):
        super().__init__(Item)
        self.price = price
    def add(self):
        self.cart.append(self.Item)
        