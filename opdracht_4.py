import os
import csv
from collections import defaultdict

def count_elements(iterable):
    d = defaultdict(int)
    for i in iterable:
        d[i] += 1
    return d


text ='appel, aap, opa, bompa, 5, True, True'
products = ""

#Write
with open("opdracht_4.txt", "w") as file:
    file.write(text)
#Read
try:
    with open("opdracht_4.txt") as file:
        file_read = file.read()
        for i in file_read:
            products += i
        products = list(products.split(","))
        print(products)
except FileNotFoundError:
    print("That file was not found")

print(count_elements(products))