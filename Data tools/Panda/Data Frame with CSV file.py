import pandas as pd 

# import CSV file

# to make a column as  index value use index_col = 'column number'
# to make a row as  a header value , skip all the row until that one. skiprow = 'row number'

df = pd.read_csv('mpg.csv',skiprows = 1 )



print df['mpg']

print df.loc[18.0]
print df.head()