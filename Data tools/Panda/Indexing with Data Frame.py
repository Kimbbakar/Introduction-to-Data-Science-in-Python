import pandas as pd 


df = pd.read_csv('mpg.csv',index_col=0,skiprows = 1 )

for i in df.columns:
	print i

print df.index
print df.head()

#################################################
print '-'*50
df = df.set_index('name')

for i in df.columns:
	print i

print df.index
print df.head() # set index remove last index row totally.

print df.head()



#################################################

print '-'*50
# index become numeric value 0...n
df  = df.reset_index()
print df.head()

df.index . name = 'ID'
print df.head()
