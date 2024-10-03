from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Derived classes
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

# Function demonstrating polymorphism
def make_sound(animal: Animal):
    print(animal.sound())

# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

# Demonstrating polymorphism
make_sound(dog)
make_sound(cat)
make_sound(cow)
