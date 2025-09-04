# herança em python

class Animal:
    name = ''
    size = ''
    color = ''

    def eat(self):
        print("Animal se alimentando")

class Horse(Animal):
    race = ''

    def escape(self):
        print("Cavalo fugindo")

class Lion(Animal):
    mane = True

    def hunt(self):
        print("Leão caçando")


h = Horse()
h.name = "Duque"
h.color = "Branco"
h.escape() # método exclusivo da classe Horse
h.eat() # método herdado da classe Animal

l = Lion()
l.name = "Simba"
l.color = "Marrom"
l.hunt() # método exclusivo da classe Lion
l.eat() 

