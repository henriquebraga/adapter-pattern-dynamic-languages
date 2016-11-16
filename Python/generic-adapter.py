
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

	def __init__(self, bird, behavior):
		self.bird = bird
		self.behavior = behavior


	def quack(self):
 		self.behavior()
	

	def __getattr__(self, attr):
 		return getattr(self.bird, attr)


if __name__ == '__main__':
	
	birds = [MallardDuck(), 
		   BirdAdapter(Turkey(), Turkey().gobble), 
		   BirdAdapter(Toucan(), Toucan().croak)]

	for bird in birds:
		bird.quack()






