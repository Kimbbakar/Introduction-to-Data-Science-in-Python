import pandas as pd 

# Use Dictionary as e data type for 

purchase_1 = pd.Series({
		'Name' : 'Chris',
		'Item Purchased': 'Dog Food',
		'Cost': 22.50
	})

purchase_2 = pd.Series ( {
		'Name' : 'Osman',
		'Item Purchased': 'abc',
		'Cost': 12.0
	})

purchase_3 = pd.Series ( {
		'Name' : 'mak',
		'Item Purchased': 'zzz',
		'Cost': 1.0
	})

df = pd.DataFrame( [purchase_1,purchase_2,purchase_3 ], index = ['Store 1','Store 1','Store 3'] )

print df 

# direct access of column 

print df ['Cost']
print df ['Item Purchased']
 
#print df.T

print df.loc[ ['Store 1']  , [ 'Name', "Cost" ] ] 

print ('-' *50)


print df.drop('Store 1') # it will drop a row

# delete column 

del df['Name']
print df

print ('-' *50)

# Add column

df ['Location'] = None

print df