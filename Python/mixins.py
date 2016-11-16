class Root:
	def call(self):
		print("My First Mixin from the chain")

	def root(self):
		print("Root mixin.")

class SecondLvl:
	def call(self):
		print("My second mixin.")

	def second(self):
		print("Level 2 mixin")

class ThirdLvl:
	def call(self):
		print("My third mixin")

	def third(self):
		print("My Level 3 mixin")

class ParentClass:
	def foo(self):
		print("This class has nothing to do with call method.")


class MixinClient(ParentClass,ThirdLvl, SecondLvl, Root):
	'''
		A example class for mixins.
		It reads from right to left < MixinClient <-- ParentClass <-- ThirdLvl <-- SecondLvl <-- Root
		So here is what we have:
[		- MixinClient extends from ParentClass;
		- ThirdLvl extends from ThirdLvl;
		- SecondLvl extends from Root;
		So when we perform method call(), it will consider the call from ThirdLvl the correct one.
	'''
	def adaptation(self):
		self.call()


if __name__ == '__main__':
	m = MixinClient()
	m.root()
	m.second()
	m.third()
	m.call()



