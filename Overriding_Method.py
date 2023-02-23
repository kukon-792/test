# Define parent class
class Parent:
    def myMethod(self):
        print("Calling parent method")

class Child(Parent): # Defint child class
    def myMethod(self):
        print("Calling child method")

c=Child()
c.myMethod()
