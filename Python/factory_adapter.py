class Cat:

	def __init__(self, name):
		self.name = name

	def meow(self):
		print(self.name + " says meow.")

class Dog:
	def __init__(self, name):
		self.name = name
	def bark(self):
		print(self.name + " says rough." )


class CatNoise():
   def __init__(self, context):
        self.context = context

   def make_noise(self):
        return self.context.meow()

class DogNoise():
    def __init__(self, context):
        self.context = context
    def make_noise(self):
    	return self.context.bark()

def noise_adapter(context):
  	"""A factory method."""
  	if isinstance(context, Cat):
  		return CatNoise(context)
  	elif isinstance(context, Dog):
  		return DogNoise(context)
  	else:
  		raise AdapterLookupError("Could not find adapter")


if __name__ == '__main__':
 	animals = [Cat('Jones'), Dog('Whoof'), Dog('Andy')]
 	for animal in animals:
 		noise_adapter(animal).make_noise()