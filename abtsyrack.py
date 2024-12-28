from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, cat):
        self.cat = cat
    @abstractmethod
    def funktion(self):
        pass

class Dog(Animal):
    def __init__(self, cat, dog):
        super().__init__(cat)
        self.dog = dog
    def funktion(self):
        return f"{self.dog} Baqradi"

class Cat(Animal):
    def __init__(self, cat, koshka):
        super().__init__(cat)
        self.koshka = koshka
    def funktion(self):
        return f"{self.koshka} deydi"

obj = Dog("animal", "it")
obj1 = Cat("animal", "koshka")

print(obj.funktion())
print(obj1.funktion())