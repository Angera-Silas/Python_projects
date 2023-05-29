class Item():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    def __init__(self, Item,p):
        super().__init__(Item)
    
        