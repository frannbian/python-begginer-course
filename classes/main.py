# Classes

#creating a class
class Animal:
    def walk(self):
        print("walking")
        
#inerithance
class Dog(Animal):
    # constructur
    def __init__(self, name, age):
        #attributes
        self.name = name
        self.age = age
        
    def bark(self):
        print("woof!")
        
#intance a class
terry = Dog("Terry", "15")

# printing attributes
print(terry.name)