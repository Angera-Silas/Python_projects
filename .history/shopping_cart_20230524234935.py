class Item():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    def __init__(self, Item,pr):
        super().__init__(Item)
    
        