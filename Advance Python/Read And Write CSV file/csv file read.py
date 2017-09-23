import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

 

cylinders = set( i['cylinders'] for i in mpg )
cylinderAvg = list()


for i in cylinders:

	cnt = 0
	val = 0 

	for j in mpg:
		if j['cylinders']==i:
			cnt = 1 + cnt
			val = val + float(i)

    
	cylinderAvg.append( (i, val/cnt ) )

cylinderAvg.sort(key = lambda x : x[0] )

print cylinderAvg