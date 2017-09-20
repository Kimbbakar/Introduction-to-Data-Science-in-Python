import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

 

print sum(float(i['weight'] ) for i in mpg ) / len(mpg)