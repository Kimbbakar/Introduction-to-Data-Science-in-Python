import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

for row in mpg:
	print row