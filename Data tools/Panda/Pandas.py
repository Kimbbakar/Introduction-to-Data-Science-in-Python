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
