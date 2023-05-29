class Items():# A class that only carries items
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Items):
    # lets create an empty list that will carry items 
    cart = []
    total = 0
    # inheriting item using a super method from the items class 
    def __init__(self,Item,price):
        self.price = price
        super().__init__(Item)
        
    def add(self):
        self.cart.append(self.Item) #adding items to cart
        print(f"{self.Item} was added successfully")
        
    def remove(self):
        self.cart.remove(self.Item)
        print(f"{self.Item} sucessfully removed")
        
    def NumberOfItems(self):
        print(f"Number of items in cart : {len(self.cart)}")
        
    def totals(self):
        carts = {}
        for item in self.cart:
            carts.update({item: self.price})
        for value in carts.values():
            self.total = self.total+
        print(f"Total Bill : {self.total}")
        
    def showcart(self):
        for i in self.cart:
            print(i)
done = False
while not done:
    try:
        choice = input("What would you like to do\n1.add\n2.remove\n3.view\n4.quit\n").lower()
        if choice =="quit":
            break
        elif choice=="add":
            Item = input("Enter item name to add : ")
            price = int(input("Enter price : "))
            customer = ShoppingCart(Item,price)
            customer.add()
            customer.NumberOfItems()
            customer.totals()
        elif choice == "remove":
            Item = input("Enter item name to remove : ")
            price = int(input("Enter price : "))
            customer = ShoppingCart(Item,(0-price))
            customer.remove(Item)
            customer.NumberOfItems()
            customer.totals()
        elif choice == "view":
            customer.NumberOfItems()
            customer.showcart()
            customer.totals()
        else:
            print("wrong input...try again")
    except:
        print("Sorry an error occured")