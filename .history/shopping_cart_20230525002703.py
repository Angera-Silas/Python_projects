class Item():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    cart = []
    def __init__(self, Item,price):
        super().__init__(Item)
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
        self.price = input
        total = total+self.price
        return total
done = False

while not done:
    choice = input("What would you like to do\n1.add\n2.remove\n3.view\n4.quit").lower()
    
    customer = ShoppingCart()
        