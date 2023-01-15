#Loops through each vegetable
#this is Python 3-3

import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

print(vegetables)    

import json

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f)


