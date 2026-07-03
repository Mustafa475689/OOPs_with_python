class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f"hello how are you {self.name}")

    def __add__(self, other):
        return(f"Your sum of ages are {self.age + other.age }")


ani = Animal("Lion", 24)
ano = Animal("dolfine", 21)
print(ani + ano)