# Decorater ..........
# class Animal:
#     @property # ye decorater obj ko call jiye bagheer bhi chla deta ha yani agar hum (obj.show() mian () nhi bhi lgay tu error hi ayga) iski example line numhber 8 pr ha.
#     def show(self):
#         print("hello how are you")

# obj = Animal()
# obj.show

# def decorate(func):
#     def wrapper(a,b): #if you don't know how many arguments you re there so you just need to replace (a,b) with (*args)
#         print("The additionof your numbers are")
#         func(a,b)
#         print("Thanks")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(f"Your total is {a + b}")

# addition(4,6)
# ...

# # args and kwargs ............. args apke arguments ko tuple form main hty hain
# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i    
#     print(sum)

# addition(2,3,4,5,6)

# # Kwargs ....................
# def information(**kwargs):
#     print("Print your information is \n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "Mustafa", age = "21", designation = "MERN dev")
# ...

# List Comphrehension ..................
# l = [i for i in range(1, 21) if i % 2 == 0]
# print(l)
# # ...

# dictionary Comphrehension ..................
# d = {i : i**2 for i in range(1, 10)}
# print(d)
# ...

# set Comphrehension ..................
# s = {i*i for i in range(1, 21) if i % 2 == 0}
# print(s)
# ...

# Lambda functions ..................
# cube = lambda i : i**3
# print(cube(2))
# checkEven = lambda i : "Even" if i % 2 == 0 else "Odd"
# print(checkEven(201021))
# ...
