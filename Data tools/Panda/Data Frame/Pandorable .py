import pandas as pd 

df = pd.read_csv('census.csv')

# chaining (ex.[][] types query) should try to be avoid
# instead of using chaining, we can query using some dot function
# this is called Pandorable

print df.where(df['SUMLEV']==50 ).head().dropna().set_index(['STNAME','CTYNAME' ] ) .rename(columns = {'ESTIMATESBASE2010' : 'Estimates Base 2010' } )