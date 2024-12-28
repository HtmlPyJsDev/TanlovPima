class Animal:
    def __init__(self, cat):
        self.cat = cat

    def speak(self):
        return f"{self.cat} ovoz chiqazadi"
    
class Dog(Animal):
    def __init__(self, cat, dog):
        super().__init__(cat)

        self.dog = dog

    def speaking(self):
        return f"{self.dog} tez yuguradi"
    
class Cat(Animal):
    def __init__(self, cat, cat2):
        super().__init__(cat)
        self.cat2 = cat2
    def speak(self):
        return f"{self.cat2} Trnaydi"
    
    
dog = Dog("Animal", "it")
cat = Cat('Animal', "mushuk")

print(dog.speak())
print(cat.speak())

# abtrak class bu umumiy sinf bolip faqat voris sinf uchun monjanlangan u obyenk yaratish uchun ishlatlmaydi abstrak class a,b,c modulidan import qb olinadi 