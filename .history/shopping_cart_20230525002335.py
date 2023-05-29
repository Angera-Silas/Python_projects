class Item():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    cart = []
    def __init__(self, Item,price):
        super().__init__(Item)
        self.price = price
    def add(self):
        self.cart.append(self.Item)
        print(f"{self.Item} was added successfully")
    def remove(self):
        self.cart.remove(self.Item)
        print(f"{self.Item} sucessfully removed")
    def NumberOfItems(self):
        return len(self.cart)
    def total(self):
        total = 0
        total = total+self.price
        return total
done = False

while not done:
    ch
    customer = ShoppingCart()
        