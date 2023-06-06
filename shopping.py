import csv
cart = []
shoppingcart = {}
# functions to add items to cart
def additem(item):
    cart.append(item)  # adding an item to the cart
    shoppingcart.update({item : 0.00})
    value = float(input(f"Enter the price of {item}"))
    shoppingcart[item] = value
    print(f"{item} has been successfully added.")
    print(f"Total Bill : {Totals()}")
def Totals():
    Total = 0
    for value in shoppingcart.values():
        Total += value
    return Total
# function to remove items from cart
def removeitem(item):
    try:
        cart.remove(item)
        del shoppingcart[item]
        print(f"{item} has been successfully removed")
    except:
        print("Sorry we could not remove the item")
# to show the cart
def showcart():
    if cart:
        print("Here is your cart")
        for key,value in shoppingcart.items():
            print(f"-{key}\t{value}")
        print(f"Total Bill : {Totals()}")
    else:
        print("Your cart is empty")
# clearing the cart
def shopping_history():
    with open("shopping.csv",mode="r",newline="") as s:
        customer = input("Confirm your username : ").title()
        print("Your shopping history")
        reader = csv.reader(s,delimiter=",")
        for row in reader:
            if customer in row:
                print(row)
def clearcart():
    cart.clear()
    shoppingcart.clear()
    print("Successfully cleared\nyour cart is empty")
def savecart():
    with open("shopping.csv",mode="a",newline="") as s:
        customer = input("Confirm your username : ").title()
        Total = Totals()
        writer = csv.writer(s,delimiter=",")
        writer.writerow([customer,shoppingcart,Total])
    print("Successfully saved your cart\nyou can view by clicking show").title()