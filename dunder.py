class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f"hello how are you {self.name}")

    def __add__(self, other):
        sum = 0 
        for i in other:
            sum = sum + i.age       
        return(f"Your sum of ages are {self.age + sum}")


ani = Animal("Lion", 24)
ano = Animal("Dolfine", 21)
ane = Animal("Tiger", 5)
print(ani + (ano, ane))
