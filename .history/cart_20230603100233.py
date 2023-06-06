import csv
def add(Item):
    with open("cart.txt",mode="w",newline="") as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow(Item)
def view():
    with open("cart.txt")
        