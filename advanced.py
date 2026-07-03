# Decorater
# class Animal:
#     @property # ye decorater obj ko call jiye bagheer bhi chla deta ha yani agar hum (obj.show() mian () nhi bhi lgay tu error hi ayga) iski example line numhber 8 pr ha.
#     def show(self):
#         print("hello how are you")

# obj = Animal()
# obj.show

def decorate(func):
    def wrapper(a,b): #if you don't know how many arguments you re there so you just need to replace (a,b) with (*args)
        print("The additionof your numbers are")
        func(a,b)
        print("Thanks")
    return wrapper

@decorate
def addition(a,b):
    print(f"Your total is {a + b}")

addition(4,6)
