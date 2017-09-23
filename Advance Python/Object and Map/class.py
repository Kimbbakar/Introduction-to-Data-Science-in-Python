
class Person:
	department = "School of Information"

	def __init__(self,name,location):
		self.name = name
		self.location = location


	def set_name(self,new_name):
		self.name = new_name

	def set_location(self,new_location):
		self.location = new_location



x = Person("osman","dhaka")




print ('{} is the name of student and he lives in {}'.format(x.name,x.location) )