import numpy as np

mylist = [1,2,3]
x = np.array(mylist)

two_D_arrya = np.array( [ [1,2],[2,3] ] )
two_D_arrya.shape


# reshape the array

#print two_D_arrya.reshape(1,4)

# add one array with other . column number need to be equal

# add vertically
print np.vstack( [two_D_arrya,2*two_D_arrya ] )
# add horizontally 
print np.hstack( [two_D_arrya,3*two_D_arrya ] )

# more operation 

# Transpose Matrix

print two_D_arrya.T
#Dot product 

print two_D_arrya.dot(two_D_arrya)

print two_D_arrya.sum()
print two_D_arrya.max()
print two_D_arrya.min()
print two_D_arrya.mean() # average 
print two_D_arrya.std() # standard  deviation. point distribution system
print two_D_arrya.argmax()
