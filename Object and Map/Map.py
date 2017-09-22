people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

x =   map( lambda x : '{} {}'.format(x.split()[0], x.split()[-1]) ,people )  
y = map ( split_title_and_name,people )


print x
print y