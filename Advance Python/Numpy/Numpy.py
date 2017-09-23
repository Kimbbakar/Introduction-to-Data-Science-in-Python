import numpy as np

mylist = [1,2,3]
x = np.array(mylist)

two_D_arrya = np.array( [ [1,2],[2,3] ] )
two_D_arrya.shape


# reshape the array

print two_D_arrya.reshape(1,4)

# add one array with other . column number need to be equal

# add vertically
print np.vstack( [two_D_arrya,2*two_D_arrya ] )
# add horizontally 
print np.hstack( [two_D_arrya,3*two_D_arrya ] )