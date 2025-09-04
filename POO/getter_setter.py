# getter e setter em python 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f'Nome {self.name} - Salário {self.__salary}')

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
            self.__salary = salary


roberto = Employee("Roberto", 4000)
roberto.show()
roberto.set_salary(5000)
roberto.show()


