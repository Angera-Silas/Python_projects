import csv
def add(Item):
    with open("cart.csv",mode="r+",newline="") as f:
        price = float(input("Enter the price : "))
        writer = csv.writer(f,delimiter=",")
        writer.writerow([Item,price])
def view():
    with open("cart.csv",mode="r",newline="") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            print(row)
