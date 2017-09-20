import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

for i in mpg[0] .keys():
	print i