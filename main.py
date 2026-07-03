#  pillars of OOPs ///////////
# Inheritance..
# Parent Class
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(f"{self.brand} {self.model} is starting...")

#     def stop(self):
#         print(f"{self.brand} {self.model} has stopped.")

#     def info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")


# # Child Class - Toyota
# class Toyota(Car):
#     def __init__(self, model):
#         super().__init__("Toyota", model)

#     def feature(self):
#         print("Toyota Feature: Excellent reliability.")


# # Child Class - Suzuki
# class Suzuki(Car):
#     def __init__(self, model):
#         super().__init__("Suzuki", model)

#     def feature(self):
#         print("Suzuki Feature: Great fuel efficiency.")


# # Child Class - Hyundai
# class Hyundai(Car):
#     def __init__(self, model):
#         super().__init__("Hyundai", model)

#     def feature(self):
#         print("Hyundai Feature: Modern technology.")


# # Creating Objects
# car1 = Toyota("Corolla")
# car2 = Suzuki("Alto")
# car3 = Hyundai("Elantra")

# # Testing
# car1.info()
# car1.start()
# car1.feature()
# print()

# car2.info()
# car2.start()
# car2.feature()
# print()

# car3.info()
# car3.start()
# car3.feature()
# ...

# 2 Polymorphism..
# class Animal:
#     def show(self):
#         print("WE are animals")

# # Method over writing
# class Human(Animal):
#     def show(self): # this show show function over writes the Animal class show function because they have same name 
#         print("Hello how are you doing")

# obj = Human()
# obj.show()

# Q) Create a parent class called Animal with a method named make_sound() that prints: Now create the following child classes: 
# Create one object of each class.

class Animal:
    def make_sound(self):
        print("Animal makes a sound")


# Child Class - Dog
class Dog(Animal):
    def make_sound(self):
        print("Dog barks: Woof Woof!")


# Child Class - Cat
class Cat(Animal):
    def make_sound(self):
        print("Cat meows: Meow!")


# Child Class - Cow
class Cow(Animal):
    def make_sound(self):
        print("Cow moos: Moo!")

# Creating Objects
animal = Animal()
dog = Dog()
cat = Cat()
cow = Cow()

# Calling Methods
animal.make_sound()
dog.make_sound()
cat.make_sound()
cow.make_sound()     
