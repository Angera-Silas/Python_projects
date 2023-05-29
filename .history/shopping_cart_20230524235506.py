class Item():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    def __init__(self, Item,price,cart=[]):
        super().__init__(Item)
        self.price = price
    def add(self):
        
        