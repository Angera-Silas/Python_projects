import csv
def add(Item):
    with open("cart.txt",mode="w",newline="") as f:
        price = float(input("Enter the price"))
        writer = csv.writer(f,delimiter=",")
        writer.writerow(Item)
def view():
    with open("cart.txt",mode="r",newline="") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            print(row)
