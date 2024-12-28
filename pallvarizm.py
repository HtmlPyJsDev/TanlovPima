class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def set_detals(self, new_name, new_salary):
        if self.__name != new_name or self.__salary:
            self.__name = new_name
            self.__salary = new_salary
    
    def get_detals(self):
        return f"menejer: {self.__name}, maosh: {self.__salary} dollar"
    

employes = Employee("Ali" 10000)