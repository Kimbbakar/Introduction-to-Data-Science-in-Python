

#option 1

my_list = []

for number in range(0,1000):
	if number % 2 == 0:
		my_list.append(number)

print my_list

# option 2 : using list comprehension

my_list = [ number for number in range(1000) if number % 2 == 0 ]



print my_list


# task

# convert this function to list comprehension 
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

lst = [ i * j for i in range(10) for j in range(10) ]
 

print lst
