class Car:
    def drive(self):
        print("Car is moving")

car1 = Car()
car1.drive()


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog:
    def sound(self):
        print("Dog barks")


a = Animal()
a.sound()
b = Dog()
b.sound()