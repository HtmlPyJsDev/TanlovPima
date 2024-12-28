class Person:
    def __init__(self, name, familia, school):
        self.name = name
        self.familia = familia
        self.school = school
    def Name2(self):
        return self.name, self.familia, self.school
class Maktab:
    def __init__(self, maktabi):
        self.maktabi = maktabi
    def maktab(self):
        return self.maktabi
class Yoshi(Maktab):
    def __init__(self, maktabi, yoshi):
        super().__init__(maktabi)
        self.yoshi = yoshi
    def Yosh(self):
        return self.yoshi
Odiy = Person('Mumtozbek', 'Qodirjanov', 6)
MaktabObj = Maktab(6)
MumtozbekYOSH = Yoshi(6, 14)
print(Odiy.Name2())  
print(MaktabObj.maktab()) 
print(MumtozbekYOSH.Yosh())  