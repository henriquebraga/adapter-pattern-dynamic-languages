
def my_def():
	print('my def')

class MallardDuck:
	def quack(self):
		print("Quack Quack.")


class Turkey:
	"""Turkey. It's not compatible with quack method :("""

	def gobble(self):
		print("Gobble gobble.")



class Toucan:
	"""Toucan. It's not compatible with quack method :("""

	def croak(self):
		print("CROAK CROAK.")


class BirdAdapter:
	"""Generic adapter."""

	def __init__(self, behavior):
		self.behavior = behavior


	def quack(self):

 		self.behavior()
	
class GenericAdapter: 
	""" A very generic adapter. It creates a function on the run, given a name and
	a function to simulate.
	Parameters:
	name: The function's name to create and satisfy the client.
	simulator: The behavior that's gonna be called when the client calls for the
	expected function. 
	"""
	def __init__(self, name, simulator):

		self.name_expected = name
		self.simulator = simulator
		setattr(self, self.name_expected, self.simulator)


if __name__ == '__main__':

	def generic_call():
		print("A generic quack to test the generic adapter.")
	
	birds = [MallardDuck(), 
		   BirdAdapter(Toucan().croak), 
		   BirdAdapter(Turkey().gobble),
		   GenericAdapter('quack', generic_call)
		   ]

	for bird in birds:
			bird.quack()










