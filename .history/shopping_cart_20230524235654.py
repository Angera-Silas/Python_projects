class Item():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    cart = []
    def __init__(self, Item,price):
        super().__init__(Item)
        self.price = price
    def add(self):
        total = 0
        self.cart.append(self.Item)
        total = tota
        