people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

for person in people:
    print(split_title_and_name(person) == (lambda x : '{} {}'.format(x.split()[0], x.split()[-1])) (person ) )


# Creating lambda function

lambda_function = lambda a,b,c : a+b

print lambda_function(1,2,3)