import csv
def add(Item):
    with open("cart.csv",mode="w",newline="") as f:
        writer = csv.writer(f,)