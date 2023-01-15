#This is Python 3-2 - CSV Files

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
 ]


#Loops through each vegetable
for veg in vegetables:
    print(veg)

#write the name of each vegetable and the color into the CSF called vegetables.csv

import csv

with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)

# this is the header row
    writer.writerow(['name', 'color'])
    len('name')


# loop through the vegetables
    for veg in vegetables:
        writer.writerow([veg['name'], veg['color']])

