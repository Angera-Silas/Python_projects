class Items():# A class that only carries items
    def __init__(self,Item):
        self.Item = Item
class ShoppingCart(Items):
    # lets create an empty list that will carry items 
    cart = []
    total = []
    sum = 0
    # inheriting item using a super method from the items class 
    def __init__(self,Item,price):
        self.price = price
        super().__init__(Item)
        
    def add(self):
        self.cart.append(self.Item) #adding items to cart
        print(f"{self.Item} was added successfully")
    #removing items from the cart    
    def remove(self):
        if self.Item in self.cart:
            self.cart.remove(self.Item)
            print(f"{self.Item} sucessfully removed")
        else:
            print("There is no such an item in the cart")
    #Displaying the total number of items in a cart
    def NumberOfItems(self):
        print(f"Number of items in cart : {len(self.cart)}")
    #Calculating the total bill of the customer    
    def totals(self):
        self.total.append(self.price)
        for i in self.total:
            self.sum+=i    
        print(f"Total bill : {self.sum}")
        
    def showcart(self):
        print(f"Number of items in cart\n{len(self.cart)}"\n)
        for i in self.cart:
            print(i)
#Main part of the program
done = False
while not done:# we loop until the customer chooses to quit
    try:
        choice = input("What would you like to do\n1.add\n2.remove\n3.view\n4.quit\n").lower()
        if choice=="add":
            Item = input("Enter item name to add : ")
            price = int(input("Enter price : "))
            customer = ShoppingCart(Item,price)
            customer.add()
            customer.NumberOfItems()
            customer.totals()
            
        elif choice == "remove":
            Item = input("Enter item name to remove : ")
            price = int(input("Enter price : "))
            price = 0 - price
            customer = ShoppingCart(Item,price)
            customer.remove()
            customer.NumberOfItems()
            customer.totals()
            
        elif choice == "view":
            customer.showcart()
                
        elif choice =="quit":
            print("Thank you for shopping with us")
            break    
        else:
            print("wrong input...try again")
    except:
        print("Sorry an error occured")