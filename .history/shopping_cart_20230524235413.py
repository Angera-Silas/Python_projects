class Item():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    def __init__(self, Item,price):
        super().__init__(Item)
        
        