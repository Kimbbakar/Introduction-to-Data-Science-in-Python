import csv

with open('new.csv') as csvfile:
    readCSV = list(csv.DictReader(csvfile))

print(readCSV[2] )