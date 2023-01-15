#Loops through each vegetable

import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

print(vegetables)    

import json

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f)
