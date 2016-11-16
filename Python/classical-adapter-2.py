"""Classical adapter solution using composition."""

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


	def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        return getattr(self.canine, attr)

class DuckObjectAdapter(Duck):
	"""Adapts by encapsulating a turkey"""

	def __init__(self, turkey):
		self._turkey = Turkey()

	def quack(self):
		self._turkey.gobble()


if __name__ == '__main__':
	birds = (MallardDuck(), DuckObjectAdapter(Turkey()))
	for bird in birds:
		bird.quack()






