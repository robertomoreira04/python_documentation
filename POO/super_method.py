# método super em python 

class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price 

    def __str__(self):
        return f"{self._brand}{self._model_name}"
    
    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para {phone_num}")


class SmarthPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price) # reaproveita os métodos da classe pai

        self.ram = ram 
        self.internal_memory = internal_memory
        self.back_camera = back_camera

Moto = Phone('Moto', 'G7', 1000)
print(Moto)
Moto.make_a_call(84996277529)
print(f"Valor do {Moto._brand}{Moto._model_name} é {Moto._price}")
print(vars(Moto)) # mostra os atributos do objeto como um dicionário

Xiaomi = SmarthPhone("Redmi ", "Note 8", 1000, "8GB", "256GB", "45MP")
print(Xiaomi)
Xiaomi.make_a_call(9823479112)
print(f"Valor do {Xiaomi._brand}{Xiaomi._model_name} é {Xiaomi._price}")
print(vars(Xiaomi))

