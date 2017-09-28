import pandas as pd 


purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
 

# Use of bool masking



#printing the name who cost more than $3
print df[ df['Cost'] >3.00] ['Name']

print ('-' *50)


# printing the name and Item who cost more than $3 but less than $6
 

print df.loc[ : ,['Name' , 'Item Purchased' ] ][( df['Cost'] >3.00) &  ( df['Cost'] <6.00) ]

print ('-' *50)

# using .where

df_cpy = df.where(df['Cost'] >3.00)
print df_cpy

# .where create some NaN column

df_cpy = df_cpy.dropna() # as the default parameter is 0 it will only NaN row.

print df_cpy

