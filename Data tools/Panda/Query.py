import pandas as pd 

# Auto indexing 

animal = ['Tiger','Bear','Moose']

print pd.Series(animal)

# indexing from dictionary 

sports = { 'Archery':'Bhutan', 'Golf':'Scotland','Sumo':'Japan','Taekwondo':'South Korea' }

print pd.Series(sports)

# explicit mention for index 


print pd.Series( ['a','b','c'], index = [ 'x','y','z' ] )

# mention in dictionary, but not mention in explicit index

name = { 'a':1,'b':2,'c':3,'d':4 }

print pd.Series(name,index=['a','c','d','z' ] )

print ('-' *50)

#Querying A Series

sports = { 'Archery':'Bhutan', 'Golf':'Scotland','Sumo':'Japan','Taekwondo':'South Korea' }
S = pd.Series(sports)

# query by index 
print S[2]
print S.iloc[2]


# query by range

print S[:3]

# query like a limited dictionary

# some time calling by index create ambiguity. 
# That is why we need to use iloc and loc.
# iloc = find the value using row number
# loc = find the value using tag 


print S.loc['Taekwondo']
print S['Golf']

