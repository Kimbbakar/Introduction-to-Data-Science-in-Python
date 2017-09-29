import pandas as pd 


df = pd.read_csv('mpg.csv',skiprows = 1 )

df  = df.reset_index()

df.index.name = "id"

df = df.set_index( [df.index,'name'] )


df . index . names = ['1st Index', '2nd Index' ]

print df.head() 
