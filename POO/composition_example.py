# composiçao em python 

class Animal:
    def __init__(self, name, category):
        self.name = name 
        self.category = category

class Fish(Animal):
    race = ""

class Parrots(Animal):
    color = ""

class Zoo:
    def __init__(self):
          # Composição: o Zoo contém objetos de Animal
        self.animals_dict = {}

    def add_animal(self, animal):
        self.animals_dict[animal.name] = animal.category

    def total_by_category(self, category):
        result = 0 
        for animal in self.animals_dict.values():
            if animal == category:
                result += 1 
        return f"No nosso zoológico temos {result} quantidade de {category}"
    
zoo = Zoo()
baleia = Fish("Nemo", "Mamíferos")
golfinho = Fish("Dory", "Mamíferos")

papagaio = Parrots("Louro", "Aves")


zoo.add_animal(baleia)
zoo.add_animal(golfinho)
zoo.add_animal(papagaio)

print(zoo.total_by_category("Aves"))
print(zoo.total_by_category("Mamíferos"))