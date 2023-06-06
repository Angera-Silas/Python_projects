import csv
def add(Item):
    with open("cart.txt",mode="w",newline="") as f:
        writter = csv.writer(f,delimiter=",")
        