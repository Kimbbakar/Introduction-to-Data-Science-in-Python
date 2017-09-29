import pandas as pd 


df = pd.read_csv('mpg.csv',skiprows = 1 )

df  = df.reset_index()

df.index.name = "id"

df = df.set_index( [df.index,'name'] )

print df.head()