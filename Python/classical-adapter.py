"""Classical adapter solution using mixings (multiple heritance)"""

class Duck:
	"""Base class (no use of ABC)"""

	def quack(self):
		pass

class MallardDuck(Duck):
	"""MallardDuck. Inherits from Duck"""

	def quack(self):
		print("Quack")


class Turkey:
	"""Turkey. It's not compatible with Duck nor quack method. :("""

	def gobble(self):
		print("Gobble gobble.")


class DuckAdapter(Duck, Turkey):
	"""Adapts a turkey to use an adapter."""

	def quack(self):
		"""It simulates a "quack", but delegating to Turkey class to perform so."""
		self.gobble()



if __name__ == '__main__':
	birds = (MallardDuck(), DuckAdapter())
	for bird in birds:
		bird.quack()






