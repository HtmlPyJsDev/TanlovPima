class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person(self):
        return self.name, self.age

class Peopre(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def schooll(self):
        return self.school
    
class Group(Peopre):
    def __init__(self, name, age, school, team):
        super().__init__(name, age, school)
        self.team = team 

    def group(self):
        return self.team

peopre = Group('g`affor', 27, '9matab', "8-d sinf")
print(peopre.group())
print(peopre.person())
print(peopre.school())

#super bu voris classdan turip yuqoridagi classni metod va atributlariga murojat qilish imkonini beradi 