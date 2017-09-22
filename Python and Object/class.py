
class Person:
	department = "School of Information"

	def set_name(self,new_name):
		self.name = new_name

	def set_location(self,new_location):
		self.location = new_location



x = Person()
x.set_name("Osman")

print x.name