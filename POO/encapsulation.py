# encapsulamento em python

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f'Nome {self.name} - Salário {self.__salary}')


roberto = Employee("Roberto", 4000)
junior = Employee("Júnior", 3500)

roberto.show()
junior.show()

roberto.__salary = 40000 # não é possível modificar

print(roberto.__dict__)
