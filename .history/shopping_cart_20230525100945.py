class Items():
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Item):
    cart = []
    def __init__(self, Item,):
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
        price = int(input("Enter price : "))
        total = total+price
        return int(total)
    def showcart(self):
        for i in self.cart:
            print(i)
done = False
while not done:
    choice = input("What would you like to do\n1.add\n2.remove\n3.view\n4.quit").lower()
    if choice =="quit":
        break
    elif choice=="add":
        Item = input("Enter item name to add : ")
        customer = ShoppingCart(Item)
        customer.add()
        customer.NumberOfItems()
    elif choice == "remove":
        Item = input("Enter item name to remove : ")
        customer.remove(Item)
        customer.NumberOfItems()
    elif choice == "view":
        customer.NumberOfItems()
        customer.showcart()
    else:
        print("error..try again")