# Multilevel inheritance
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class BabyDog(Dog):
    def weep(self):
        print("Weeeping...")

d=BabyDog()
d.eat()
d.bark()
d.weep()